###############################################################################
# Functions to convert text copy/pasted from bb majors website into dictionary
# of player costs
###############################################################################

# Assumes website player costs has been copy/pasted from bb majors website
def create_costs_dict(raw_costs_str):
    lines_list = raw_costs_str.split('\n')
    costs_dict = {}
    for line in lines_list:
        words = line.split()

        # Remove any trailing junk before the numeric cost
        while words and not words[-1].isnumeric():
            del words[-1]
        
        # Remomve any leading whitespace
        if words:
            words[0] = words[0].strip()
            full_name = ' '.join(words[:-1])
            costs_dict[full_name] = float(words[-1])
        
    return costs_dict
