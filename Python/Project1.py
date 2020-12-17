import sys

# 학점 계산 함수---------------------------------------------------------------------
def grades(mid, final):
    mid=int(mid)
    final=int(final)
    score=(mid+final)/2    # 평균 계산
    if score>=90:
        grade='A'
    elif score>=80:
        grade='B'
    elif score>=70:
        grade='C'
    elif score>=60:
        grade='D'
    else:
        grade='F'
    return score,grade    # 학점과 평균을 반환

# 전체 학생 출력 함수------------------------------------------------------------------
def print_info():
    stu_info.sort(key=lambda x:x[4],reverse=True)    # 평균을 기준으로 정렬
    print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
    print('--------------------------------------------------------------')
    for i in stu_info:
        for j in i:
            print(j, end='\t')
        print()

# 일부 학생 출력 함수-----------------------------------------------------------------
def print_stu_info(stu_id):    # 출력시킬 학생의 학번을 입력받음
    for i in range(len(stu_info)):
        if stu_info[i][0]==stu_id:   
            print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
            print('--------------------------------------------------------------')
            for j in stu_info[i]:
                print(j, end='\t')
            print()
            return i    # 몇 번째 학생인지 반환

# 학생의 학번 존재 유무 확인 함수
def if_stu_val(stu_id):
    stu_num_array=[]
    for s in stu_info:
        stu_num_array.append(s[0])
    if stu_id not in stu_num_array:    # 존재하지 않는 학생일 때
        return False
    else:
        return True
        
# 파일 읽기--------------------------------------------------------------------------
# 우선 읽어들일 파일을 입력받고 파일을 오픈한다.
order_num=len(sys.argv)
if order_num==1:
    fr_name="students.txt"
else:
    fr_name=sys.argv[1]
fr=open(fr_name,'r')

# 텍스트 파일로부터 데이터를 읽어 리스트 목록으로 저장
stu_info=[]
for line in fr:
    line=line[:-1]
    line=line.split('\t')
    score,grade=grades(line[2], line[3])
    line.append(score)
    line.append(grade)
    stu_info.append(line)
print_info()

# 명령어 리스트
order_list=['show','search','changescore','searchgrade','add','remove','quit']
# 사용자 명령어 입력 시작---------------------------------------------------------------
while True:
    order=input('# ').lower()    # 사용자의 명령어 입력
    if order not in order_list:
        continue
    # show (전체 학생 정보 출력)-------------------------------------------------------
    if order=='show':
        print_info()
    # search (특정 학생 검색)---------------------------------------------------------
    elif order=='search':
        stu_id=input('Student ID: ')    
        if not if_stu_val(stu_id):    # 존재하지 않는 학생이면
            print('NO SUCH PERSON.')
            continue
        print_stu_info(stu_id)
    # changescore (점수 수정)--------------------------------------------------------
    elif order=='changescore':
        stu_id=input('Student ID: ')
        if not if_stu_val(stu_id):    # 존재하지 않는 학생이면
            print('NO SUCH PERSON.')
            continue
        else:
            mf=input('Mid/Final? ')
            if mf not in ['mid', 'final']:
                print('Wrong Input')
                continue
            new_score=int(input('Input new score: '))
            if new_score <0 or new_score>100:
                print('Wrong score')
                continue
            stu_num=print_stu_info(stu_id)
            if mf=='mid':
                stu_info[stu_num][2]=new_score
            else:
                stu_info[stu_num][3]=new_score
            score,grade=grades(stu_info[stu_num][2],stu_info[stu_num][3])
            stu_info[stu_num][4]=score
            stu_info[stu_num][5]=grade
            print('Score changed')
            for j in stu_info[stu_num]:
                print(j, end='\t')
            print()
    # add (학생 추가)----------------------------------------------------------------
    elif order=='add':
        stu_id=input('Student ID: ')
        if if_stu_val(stu_id):    # 이미 존재하는 학생이면
            print('ALREADY EXISTS.')
            continue
        stu_name=input('Name: ')
        mid=input('Midterm Score: ')
        final=input('Final Score: ')
        score, grade=grades(mid,final)
        stu_info.append([stu_id,stu_name,mid,final,score,grade])
        print('Student added.')
    # searchgrade (Grade 검색)------------------------------------------------------
    elif order=='searchgrade':
        grade=input('Grade to search: ')
        array=[]
        if grade not in ['A','B','C','D','F']:   # A/B/C/D/F 외의 값이 입력된 경우
            continue
        for i in range(len(stu_info)):
            if stu_info[i][5]==grade:
                array.append(i)
        if len(array)==0:    # 해당 grade의 학생이 없는 경우
            print('NO RESULTS.')
        else:
            print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
            print('--------------------------------------------------------------')
            for student in stu_info:
                if student[5]!=grade:
                    continue
                for j in student:
                    print(j, end='\t')
                print()
    # remove (특정 학생 삭제)-------------------------------------------------------- 
    elif order=='remove':
        if len(stu_info)==0:    # 목록에 아무도 없을 경우
            print('List is empty.')
            continue
        stu_id=input('Student ID: ')
        if not if_stu_val(stu_id):
            print('NO SUCH PERSON.')
            continue
        for i in range(len(stu_info)):
            if stu_info[i][0]==stu_id:
                del(stu_info[i])
                print('Student removed.')
                break
    # quit (종료)------------------------------------------------------------------
    elif order=='quit':
        reply=input('Save data?[yes/no] ').lower()
        if reply=='yes':
            fw_name=input('File name: ')    # 저장할 파일명 입력 받기
            fw=open(fw_name,'w')    # 파일 OPEN
            for s in stu_info:
                array=s[0]+'\t'+s[1]+'\t'+str(s[2])+'\t'+str(s[3])+'\n'
                fw.write(array)
            print("Saved. Bye!")
            break
        else:
            print("No saved. Bye!")
            break
