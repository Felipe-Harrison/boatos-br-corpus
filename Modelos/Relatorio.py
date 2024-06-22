def formatReport(report: list[dict],accuracy: float):
    labels = ['falso','verdade']
    report_final = []
    for label in labels:
        keys = report[label].keys()
        for key in keys:
            report_final.append(str(report[label][key]).replace('.',','))
    report_final.append(str(accuracy).replace('.',','))
    return ";".join(report_final)