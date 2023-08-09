# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"2FG5.00","system":"readv2"},{"code":"M260000","system":"readv2"},{"code":"M261000","system":"readv2"},{"code":"M261100","system":"readv2"},{"code":"M261200","system":"readv2"},{"code":"M261300","system":"readv2"},{"code":"M261400","system":"readv2"},{"code":"M261500","system":"readv2"},{"code":"M261600","system":"readv2"},{"code":"M261900","system":"readv2"},{"code":"M261A00","system":"readv2"},{"code":"M261B00","system":"readv2"},{"code":"M261C00","system":"readv2"},{"code":"M261F00","system":"readv2"},{"code":"M261G00","system":"readv2"},{"code":"N25..00","system":"readv2"},{"code":"10183.0","system":"med"},{"code":"107861.0","system":"med"},{"code":"15609.0","system":"med"},{"code":"15655.0","system":"med"},{"code":"1654.0","system":"med"},{"code":"17895.0","system":"med"},{"code":"20164.0","system":"med"},{"code":"21182.0","system":"med"},{"code":"25590.0","system":"med"},{"code":"25737.0","system":"med"},{"code":"31828.0","system":"med"},{"code":"32041.0","system":"med"},{"code":"33367.0","system":"med"},{"code":"34937.0","system":"med"},{"code":"379.0","system":"med"},{"code":"4065.0","system":"med"},{"code":"4360.0","system":"med"},{"code":"43811.0","system":"med"},{"code":"48105.0","system":"med"},{"code":"52909.0","system":"med"},{"code":"53994.0","system":"med"},{"code":"54566.0","system":"med"},{"code":"55983.0","system":"med"},{"code":"67453.0","system":"med"},{"code":"72243.0","system":"med"},{"code":"8065.0","system":"med"},{"code":"9008.0","system":"med"},{"code":"9058.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('acne-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acne---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acne---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acne---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
