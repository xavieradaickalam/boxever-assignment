#!/usr/bin/env python
from argparse import ArgumentParser


def analyse_customer_satisfaction(seat_arrangement,groups):
    same_row = True
    window_seat = True
    for group in groups:
        row_of_group = []
        for m in range(len(group)):
            for i in range(len(seat_arrangement)):
                for j in range(len(seat_arrangement[i])):
                    if group[m] == seat_arrangement[i][j]:
                        row_of_group.append(i)
                        if 'W' in group[m]:
                            window_seat = window_seat and (j == 0 or j == len(seat_arrangement[i]) - 1)
        same_row = same_row and (row_of_group.count(row_of_group[0]) == len(row_of_group))
    return same_row and window_seat


def read_file(file_name):
    file_content = []
    with open(file_name) as f:
        line = f.readline().rstrip()
        file_content.append(line)
        while line:
            line = f.readline().rstrip()
            file_content.append(line)
    file_content.pop()
    #print (file_content)
    seat_map = file_content.pop(0).split()
    seats_in_row = int(seat_map[0])
    rows = int(seat_map[1])
    groups = create_passengers_group(file_content)
    #print 'Groups :', groups
    seat_arrangement = allocate_seats(groups, seats_in_row, rows)
    #print (seat_arrangement)
    seat_arrangement = allocate_window_seats(seat_arrangement, seats_in_row, rows)
    customer_satisfaction = analyse_customer_satisfaction(seat_arrangement, groups)
    print_result(seat_arrangement, customer_satisfaction)


def print_result(seat_arrangement, customer_satisfaction):
    for row in seat_arrangement:
        print ''.join([str(passenger + ' ') for passenger in row])
    if customer_satisfaction:
        print ('100%')

def create_passengers_group(file_content):
    groups = []
    for line in file_content:
        group = line.split()
        groups.append(group)
    return groups


def allocate_window_seats(seat_arrangement, seats_in_row, rows):
    result_seat_arrangement = [['0' for x in range(seats_in_row)] for y in range(rows)]
    current_row_count = 0
    for seating_row in seat_arrangement:
        current_row = seating_row
        result_row = ['0' for x in range(seats_in_row)]
        #print current_row
        for passenger in current_row:
            if 'W' in passenger:
                if result_row[0] == '0':
                    result_row[0] = passenger
                elif result_row[len(result_row)-1] == '0':
                    result_row[len(result_row)-1] = passenger
        for passenger in current_row:
            if 'W' not in passenger:
                for i in range(0, len(result_row)):
                    if result_row[i] == '0':
                        result_row[i] = passenger
                        break
        #print (result_row)
        result_seat_arrangement[current_row_count] = result_row
        current_row_count = current_row_count + 1
    return result_seat_arrangement


def allocate_seats(groups, seats_in_row, rows):
    seat_arrangement = [['0' for x in range(seats_in_row)] for y in range(rows)]
    #print seat_arrangement
    for group in groups:
        current_row = -1
        for seating_row in seat_arrangement:
            current_row = current_row + 1
            empty_seat_count = seating_row.count('0')
            #print 'empty_seat_count :', empty_seat_count
            if empty_seat_count > 0:
                break
        #print 'current row :', current_row
        empty_seats = seat_arrangement[current_row].count('0')
        #print ('empty_seats' + str(empty_seats))
        if empty_seats == len(group):
            current_data = seat_arrangement[current_row]
            current_zero_index = - 1
            for i in range(len(current_data)):
                if current_data[i] == '0':
                    current_zero_index = i
                    break
            for j in range(len(group)):
                current_data[current_zero_index] = group[j]
                current_zero_index = current_zero_index + 1
            seat_arrangement[current_row] = current_data
        elif empty_seats > len(group):
            current_data = seat_arrangement[current_row]
            for i in range(len(group)):
                current_data[i] = group[i]
            seat_arrangement[current_row] = current_data
        elif empty_seats < len(group) and current_row < (rows-1):
            seat_arrangement[current_row + 1] = group
        #print seat_arrangement
    return seat_arrangement


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('-i', type=str, default='input-data.txt', help='input file containing seat layout and passenger group with seating preferences')
    args = arg_parser.parse_args()
    read_file(args.i)


if __name__ == '__main__':
    main()