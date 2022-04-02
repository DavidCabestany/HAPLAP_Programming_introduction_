def transportation(rain,km):
    if rain == 'no':
        if km < 2:
            return 'Better to walk.'
        elif km >= 2 and km <= 10:
            return 'Better to ride a bike.'
    if rain != 'no' or km > 10:
        return 'Better to go by bus.'



