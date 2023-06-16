def detect_sport(equipment):
    match equipment:
        case num if 0 <= num <= 2:
            return "archery"
        case num if 3 <= num <= 5:
            return "baseball"
        case num if 6 <= num <= 7:
            return "basketball"
        case num if 8 <= num <= 11:
            return "billiards"
        case num if 12 <= num <= 13:
            return "carrom"
        case num if 14 <= num <= 15:
            return "chess"
        case num if 16 <= num <= 20:
            return "cricket"
        case num if 21 <= num <= 23:
            return "golf"
        case num if 24 == num:
            return "rugby"
        case num if 25 <= num <= 26:
            return "tennis"
        case default:
            return ""
