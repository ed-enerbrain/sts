import filler


def assertion(checks, responses):
    results = []
    for check in checks:
        filled_check = filler.fill_regex(check, responses)
        check_result = eval(filled_check)
        print(f'check {check} >>> {filled_check} : {check_result}')
        results.append({
            "check": check,
            "filled_check": filled_check,
            "result": check_result
        })

    checks_results = list(map(lambda x: x['result'], results))

    return {
        "type": "ASSERT",
        "summary": {
            "total": len(checks_results),
            "passed": checks_results.count(True),
            "failed": checks_results.count(False)
        },
        "results": results
    }
