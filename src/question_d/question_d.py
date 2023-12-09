def list_matching_contiguous_locations(dna1, dna2):
    location_list = []
    num = 0
    while num < len(dna1):
        if dna1.find(dna2, num, len(dna1)+1) >= 1 and dna1.find(dna2, num, len(dna1))+1 not in location_list:
            location_list.append(dna1.find(dna2, num, len(dna1))+1)
        num += 1
    return location_list

def build_dna_sequence_01(user_input, stop_clause):
    acceptable_list = ['A', 'G', 'T', 'C']
    compiling_dna1 = []
    min_dna1 = 8
    max_dna1 = 16
    while user_input.upper() in acceptable_list and (len(compiling_dna1) < min_dna1 or len(compiling_dna1) > max_dna1) and user_input.upper() != stop_clause:
        print('You can add ' + acceptable_list + 'until you have at least ' + min_dna1 + ' and less than '+ max_dna1)
        
        if user_input.upper() in acceptable_list and len(compiling_dna1)+1 < max_dna1:
            compiling_dna1.append(user_input.upper())
            print('\tDNA strand added.\n\tCurrent strand list: ' + compiling_dna1)
        elif user_input.upper() in acceptable_list and len(compiling_dna1)+1 > max_dna1:
            print('\tToo many characters for dna sequence 1. Please delete some to add more.')
