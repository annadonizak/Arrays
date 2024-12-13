###
# Prints vehicle registration numbers from Krakow
#
polish_license_plates = [
   'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
   'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
   'KK54985', 'LU4864U'
]

def print_krk_plates(plates):
    counter = 1
    for car_number in plates:
       if car_number[:2] in ['KR', 'KK']:
          print(counter, car_number)
          counter += 1


def main():
    print_krk_plates(plates=polish_license_plates)
    

if __name__ == '__main__':
    main()