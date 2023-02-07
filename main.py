def main():
    ##################################################
    # Comlete your code here
    reg_hours = int(40)
    reg_rate = float(18.25)
    o_rate = float(27.78)
    workhours = int(input('How many hours did you work this week? '))
    if workhours > reg_hours:
        o_hours = workhours - reg_hours
        reg_charge = reg_rate * reg_hours
        o_charge = o_hours * o_rate
        total_wage = reg_charge + o_charge
    if workhours > reg_hours:
        print ('Regular Charge : $', reg_charge,
        '\nOvertime Charge : $', o_charge,
        '\nTotal Wage : $', total_wage)
    if workhours <= reg_hours:
        print ('Total Wage : $', workhours * reg_rate)
    ##################################################
    pass


if __name__ == '__main__':
    main()
