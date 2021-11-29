from pytest_bdd import scenarios, given, when, then, parsers
from retirementAgeCalculator import RetirementAgeCalculator
EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'year': int,
    'month': int,
    'retireAge': int,
    'addMonths': int,
    'retireYear': int,
}
    pass



@scenarios("../features/retirement.feature", example_converters=CONVERTERS)
def test_retirement():

###############################################################################################

@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year_month2(year, month):
    return RetirementAgeCalculator(year, month)


@when("the year of retirement is returned")
def get_year_of_retirement(birth_year_month2):
    return birth_year_month2.year_of_retirement


@then(parsers.cfparse("verify the year is equals '{expected_year:number}'", extra_types=EXTRA_TYPES))
def verify_year_of_retirement(get_year_of_retirement, expected_year):
    assert get_year_of_retirement == expected_year

#######################################################################################################

@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year_month1(year, month):
    return RetirementAgeCalculator(year, month)


@when("the retire age is returned")
def get_retire_age(birth_year_month1):
    return birth_year_month1.retire_age


@then(parsers.cfparse("verify the age is equals '{expected:number}'", extra_types=EXTRA_TYPES))
def verify_age(get_retire_age, expected):
    assert get_retire_age == expected







###########################################################################################################

@given(parsers.cfparse("the year and month of birth '{year:number}', '{month:number}'", extra_types=EXTRA_TYPES))
def birth_year(year, month):
    return RetirementAgeCalculator(year, month)


@when("the year of retirement is returned")
def get_year_of_retirement(birth_year):
    return birth_year.retire_retire_age


@then(parsers.cfparse("the program returns an error, and it displays the user “Year must be 1900 or above” '{expected_add_month:number}'", extra_types=EXTRA_TYPES))
def verify_yearRange(get_year_of_retirement, expected_year):
    assert get_year_of_retirement, expected_year





