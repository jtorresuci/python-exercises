def main():

    # Open babynames.txt for reading
    infile = open("babynames.txt", "r")

    # Open boy and girl names text files for writing
    out_boys = open("boynames.txt", "w")
    out_girls = open("girlnames.txt", "w")
    for line in infile:
        # Split line
        names = line.split()

        # Concatenate line to write for boys and girls
        boy_line = names[1] + "\n"
        girl_line = names[3] + "\n"

        # Write to respective files
        out_boys.write(boy_line)
        out_girls.write(girl_line)
    
    # Done processing, -> close opened files
    infile.close()
    out_boys.close()
    out_girls.close()
    
    # Open boy and girl files for reading
    boy_infile = open("boynames.txt", "r")
    girl_infile = open("girlnames.txt", "r")

    # Return a list containing boy and girl names \n character included
    line_boys = boy_infile.readlines()
    line_girls = girl_infile.readlines()

    # Iterate and print top 10 boy names
    print("Top 10 most popular baby boy names for 2011:")
    for i in range(10):
        print(line_boys[i], end = "")

    # Iterate and print top 10 girl names
    print("\nTop 10 most popular baby girl names for 2011:")
    for i in range(10):
        print(line_girls[i], end = "")

main()