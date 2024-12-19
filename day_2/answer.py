import os


def main():
    reports = get_lists_from_input()
    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports += 1
    print("%s safe reports" % safe_reports)
    safe_with_one_removed = 0
    import time
    start_time = time.time()
    for report in reports:
        if is_report_safe_with_one_removed(report):
            safe_with_one_removed += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time doing brute force: {elapsed_time * 1000} miliseconds")
    print("%s safe reports with one removed" % safe_with_one_removed)



def get_lists_from_input(input_file_name=None):
    if input_file_name is None:
        input_file_name = "input.txt"
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        input_file_name = os.path.join(__location__, input_file_name)

    with open(input_file_name) as input_file:
        contents = input_file.read()
    lists = [[int(number) for number in line.split()] for line in contents.split('\n')]
    return lists


def is_report_safe(report):
    if len(report) < 2:
        print("Really short report")
        breakpoint()
    if report[0] == report[1]:
        return False
    rising = report[0] < report[1]
    for index in range(len(report) - 1):
        difference = report[index + 1] - report[index]
        if rising:
            if difference < 1 or difference > 3:
                return False
        else:
            if difference > -1 or difference < -3:
                return False
    return True


def remove_index_and_try_again(report, bad_index):
    _report = report[:]
    _report.pop(bad_index)
    is_safe = is_report_safe(_report)
    return is_safe


def is_report_safe_with_one_removed(report):
    can_be_saved = is_report_safe(report) or any([remove_index_and_try_again(report, index) for index in range(len(report))])
    return can_be_saved


if __name__ == '__main__':
    main()
