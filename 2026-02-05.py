def c_score(std):
    toral = std["국어"] + std["영어"] + std["수학"]
    avg = toral / 3
    std["총점"] = toral
    std["평균"] = avg

def t_std(stds):
    f_std = None
    f_avg = 0

    for std in stds.values():
        if std["평균"] > f_avg:
            f_avg = std["평균"]
            f_std = std["이름"]

    return f_std, f_avg

stds = {
    "std1": {"이름": "김철수", "국어": 85, "영어": 90, "수학": 95},
    "std2": {"이름": "이영희", "국어": 88, "영어": 92, "수학": 84},
    "std3": {"이름": "박민수", "국어": 90, "영어": 85, "수학": 88},
}

print("=== 학생 성적 관리 ===")

for std in stds.values():
    c_score(std)
    print(f"{std["이름"]}점, 영어 : {std["영어"]}점, 수학 : {std["수학"]}점")
    print(f"총점 : {std["총점"]}점, 평균 : {std["평균"]:.2f}점")
    print("---")

name, avg = t_std(stds)
print(f"최고 평균 학생 : {name}, 평균 : {avg:.2f}점")
