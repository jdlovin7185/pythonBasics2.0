the_runway = "im with fuck face"
fuel = "high"


def is_runway_free(runway, fuel_status):
    if runway == "free":
        return "Land"
    elif fuel_status == "low":
        return "Emergency landing"
    else:
        return "Figure it out"


print(is_runway_free(the_runway, fuel))
