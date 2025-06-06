if __name__ != "__main__":
    from autograder_assistant import input


def read_data(file_name):
    input_file = open(file_name, "r")
    s_strand = input_file.readline()
    input_file.close()
    s_strand = s_strand.strip()
    return s_strand

def is_valid_strand(s_strand):
    b_valid = True
    for base in s_strand:
        if base != 'A' and base != 'C' and base != 'G' and base != 'T':
            b_valid = False
    return b_valid

def num_differences(s_strand1, s_strand2):
    diffs = 0
    for index in range(len(s_strand1)):
        if s_strand1[index] != s_strand2[index]:
            diffs = diffs + 1
    return diffs

def complement(s_strand):
    comp = ""
    for base in s_strand:
        if base == "A":
            comp = comp + "T"
        elif base == "C":
            comp = comp + "G"
        elif base == "G":
            comp = comp + "C"
        else:
            comp = comp + "A"
    return comp

def get_triplets(s_strand):
    l_triplets = []
    counter = 0
    num_triplets = len(s_strand) // 3
    for index in range(num_triplets):
        s_trip = ""
        s_trip = s_trip + s_strand[counter]
        counter = counter + 1
        s_trip = s_trip + s_strand[counter]
        counter = counter + 1
        s_trip = s_trip + s_strand[counter]
        counter = counter + 1
        l_triplets.append(s_trip)
    return l_triplets
        

def get_amino_acids(l_triplets):
    am_acid = ""
    for s_trip in l_triplets:
        am_acid = am_acid + get_acid(s_trip)
    return am_acid
        

def get_acid(s_triplet):
    acid = ""
    if s_triplet[0] == "T":
        if s_triplet[1] == "T":
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "F"
            else:
                acid = "L"
        elif s_triplet[1] == "C":
                acid = "S"
        elif s_triplet[1] == "A":
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "Y"
            else:
                acid = "*"
        if s_triplet[1] == "G":
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "C"
            elif s_triplet[2] == "A":
                acid = "*"
            else:
                acid = "W"
        
    elif s_triplet[0] == "C":
        if s_triplet[1] == "T":
            acid = "L"
        elif s_triplet[1] == "C":
            acid = "P"
        elif s_triplet[1] == "A":
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "H"
            else:
                acid = "Q"
        else:
            acid = "R"
            
    elif s_triplet[0] == "A":
        if s_triplet[1] == "T":
            if s_triplet[2] == "G":
                acid = "M"
            else:
                acid = "I"
        elif s_triplet[1] == "C":
            acid = "T"
        elif s_triplet[1] == "A":
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "N"
            else:
                acid = "K"
        else:
            if s_triplet[2] == "T" or s_triplet[2] == "C":
                acid = "S"
            else:
                acid = "R"    
    elif s_triplet[0] == "G":
        if s_triplet[1] == "T":
            acid = "V"
        elif s_triplet[1] == "C":
            acid = "A"        
        elif s_triplet[1] == "A":
            acid = "D"
        else:
            acid = "G"
            
    return acid
            
    


def main():
    print()
    p_strand = read_data("possum.txt")
    m_strand = read_data("mouse.txt")
    b_p_valid = is_valid_strand(p_strand)
    b_m_valid = is_valid_strand(m_strand)
    if b_m_valid == True and b_m_valid == True:
        print("Both strands are valid")
        num_diffs = num_differences(p_strand, m_strand)
        print("Strands differ in", num_diffs, "places.")
        print(m_strand, "mouse")
        print(complement(m_strand), "mouse-complement")
        print(p_strand, "possum")
        print(complement(p_strand), "possum-complement")
        m_trip = get_triplets(m_strand)
        p_trip = get_triplets(p_strand)
        m_acid = get_amino_acids(m_trip)
        p_acid = get_amino_acids(p_trip)
        print(m_acid, "mouse")
        print(p_acid, "possum")
    else:
        if b_m_valid == False:
            print("mouse strand invalid")
        if b_p_valid == False:
            print("possum strand invalid")
    

if __name__ == "__main__":
    main()
