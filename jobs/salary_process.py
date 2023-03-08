import re


def salary_hh_process(salary):
    try:
        if len(salary) == 1:
            return salary[0]
        result = {}
        salary_condition = salary[-1]
        salary = list(map(lambda x: re.sub(r'\W', '', x), salary[:-1]))
        if len(salary) == 7:
            result["salary_from"] = int(salary[1])
            result["salary_to"] = int(salary[3])
            result["salary_currency"] = salary[5]
        else:
            if salary[0] == 'от':
                result["salary_from"] = int(salary[1])
            elif salary[0] == 'до':
                result["salary_to"] = int(salary[1])
            result["salary_currency"] = salary[3]
        result["salary_condition"] = salary_condition
        return result
    except:
        return salary
    pass


def salary_sj_process(salary):
    try:
        if len(salary) == 1:
            return salary[0]
        result = {}
        salary = list(map(lambda x: x.replace('\xa0', ''), salary))
        if '—' in salary:
            result["salary_from"] = int(salary[0])
            result["salary_to"] = int(salary[4])
            result["salary_currency"] = salary[-2]
        elif 'от' in salary or 'до' in salary:
            if 'от' in salary:
                result["salary_from"] = int(salary[2][:-1])
            else:
                result["salary_to"] = int(salary[2][:-1])
            result["salary_currency"] = salary[2][-1]
        else:
            result["salary_amount"] = int(salary[0])
            result["salary_currency"] = salary[2]
        result["salary_condition"] = salary[-1]
        return result
    except:
        return salary


# superjob
# s1 = ['150\xa0000', '\xa0', '—', ' ', '200\xa0000', '\xa0', '₽', 'месяц']
# s2 = ['По договорённости']
# s3 = ['150\xa0000', '\xa0', '—', ' ', '220\xa0000', '\xa0', '₽', 'месяц']
# s4 = ['от', '\xa0', '15\xa0000\xa0₽', 'месяц']
# s5 = ['60\xa0000', '\xa0', '₽', 'месяц']
# s6 = ['до', '\xa0', '150\xa0000\xa0₽', 'месяц']
# print(salary_sj_process(s1))
# print(salary_sj_process(s2))
# print(salary_sj_process(s3))
# print(salary_sj_process(s4))
# print(salary_sj_process(s5))
# print(salary_sj_process(s6))

# hh.ru
# salary1 = ['от ', '40\xa0000', ' до ', '60\xa0000', ' ', 'руб.', ' ', 'на руки']
# salary2 = ['до ', '172\xa0500', ' ', 'руб.', ' ', 'до вычета налогов']
# salary3 = ['от ', '70\xa0000', ' ', 'руб.', ' ', 'на руки']
# salary4 = ['от ', '90\xa0000', ' ', 'руб.', ' ', 'до вычета налогов']
# salary5 = ['з/п не указана']
# salary6 = ['до ', '165\xa0000', ' ', 'руб.', ' ', 'до вычета налогов']
#
# print(salary_process(salary1))
# print(salary_process(salary2))
# print(salary_process(salary3))
# print(salary_process(salary4))
# print(salary_process(salary5))
# print(salary_process(salary6))
