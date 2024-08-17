def Z18733(Z18733K1):
    # define the units and twenties place
    ones = ["", "bat", "bi", "hiru", "lau", "bost", "sei", "zazpi", "zortzi", "bederatzi", "hamar", "hamaika", "hamabi", "hamahiru", "hamalau", "hamabost", "hamasei", "hamazazpi", "hamazortzi", "hemeretzi"]
    twenties = ["", "hogei", "berrogei", "hirurogei", "laurogei"]
    hundreds = ["", "ehun", "berrehun", "hirurehun", "laurehun", "bostehun", "seiehun", "zazpiehun", "zortziehun", "bederatziehun"]
    units = [("kuaturdezilioi", 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),("tredezilioi", 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000),("duodezilioi", 1_000_000_000_000_000_000_000_000_000_000_000_000_000),("undezilioi", 1_000_000_000_000_000_000_000_000_000_000_000_000),("dezilioi", 1_000_000_000_000_000_000_000_000_000_000_000),("nonilioi", 1_000_000_000_000_000_000_000_000_000_000),("oktilioi", 1_000_000_000_000_000_000_000_000_000),("septilioi", 1_000_000_000_000_000_000_000_000),("sextilioi", 1_000_000_000_000_000_000_000),("kintilioi", 1_000_000_000_000_000_000), ("kuadrilioi", 1_000_000_000_000_000), ("trilioi", 1_000_000_000_000), ("bilioi", 1_000_000_000), ("milioi", 1_000_000), ("mila", 1_000), ("ehun", 100), ("", 1)]

    # function to convert numbers less than 1000 to words
    def words(Z18733K1):
        if Z18733K1 == 0:
            return ""
        elif Z18733K1 <= 19:
            return ones[Z18733K1]
        elif Z18733K1 <= 99:
            twenties_unit = twenties[Z18733K1 // 20]
            ones_unit = ones[Z18733K1 % 20]
            return twenties_unit + "ta " + ones_unit if ones_unit else twenties_unit
        else:
            return hundreds[Z18733K1 // 100] + " eta " + words(Z18733K1 % 100) if Z18733K1 % 100 else hundreds[Z18733K1 // 100]

    # convert numbers to words
    result = ""
    if Z18733K1 < 0:
        Z18733K1 = abs(Z18733K1)
        result = "minus"
    if Z18733K1 == 0:
        result = "zero"
    else:
        for unit_name, factor in units:
            count, Z18733K1 = divmod(Z18733K1, factor)
            if count > 999:
                #ERROR: number is too large for this algorithm
                result = "ERROREA: zenbakia handiegia da algoritmo honetarako"
            if count > 0:
                if factor == 1000:
                    result = result + " " + words(count) + " " + unit_name if count != 1 else result + " " + unit_name
                elif factor == 100:
                    if (Z18733K1 % factor):
                        result = result  + " " + hundreds[count]
                    else:
                        result = result + " eta " + hundreds[count]
                elif factor == 1:
                    result = result + " eta " + words(count) + unit_name
                else:
                    result = result + " " + words(count) + " " + unit_name if count != 1 else result + " " + unit_name + " bat"
        if (result.startswith(" eta ")): result = result[5:]
        elif (result.startswith("minus eta ")): result = result.replace("minus eta ","minus ")
    return result.strip()
