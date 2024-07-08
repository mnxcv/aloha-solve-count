import requests
import problems
import members

class API:
    base_url = "https://solved.ac/api/v3"

    @classmethod
    def solve_count(cls, id_, level):
        url_prefix = cls.base_url + f"/search/problem?query=solved_by%3A{id_}%26%28"
        url_suffix = "%29"
        to_find_basic = ""
        for problem in problems.problems[level]["basic"]:
            to_find_basic += f"id%3A{str(problem)}"
            if problem != problems.problems[level]["basic"][-1]:
                to_find_basic += "%7C"
        to_find_basic = url_prefix + to_find_basic + url_suffix

        to_find_intermediate = ""
        for problem in problems.problems[level]["intermediate"]:
            to_find_intermediate += f"id%3A{str(problem)}"
            if problem != problems.problems[level]["intermediate"][-1]:
                to_find_intermediate += "%7C"
        to_find_intermediate = url_prefix + to_find_intermediate + url_suffix
        
        basic_count = requests.get(to_find_basic).json()["count"]
        intermediate_count = requests.get(to_find_intermediate).json()["count"]

        return basic_count, intermediate_count

def main():
    csv_file = open("solved.csv", "w")
    csv_file.write("조, 이름, 핸들, 초급반 필수, 초급반 심화, 중급반 필수, 중급반 심화\n")

    for member in members.members:
        print(f"Processing {member}")
        e_basic, e_intermediate = API.solve_count(member, "easy")
        h_basic, h_intermediate = API.solve_count(member, "hard")
        csv_file.write(f"0, 0, {member}, {e_basic}, {e_intermediate}, {h_basic}, {h_intermediate}\n")

def test_one(member):
    e_basic, e_intermediate = API.solve_count(member, "easy")
    h_basic, h_intermediate = API.solve_count(member, "hard")
    print(f"0, 0, {member}, {e_basic}, {e_intermediate}, {h_basic}, {h_intermediate}")

#test_one("mnx")

if __name__ == "__main__":
    main()