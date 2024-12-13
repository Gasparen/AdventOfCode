

def read_file():
    f = open('inputs/day5_indata.txt', 'r')
    #f = open('day5_testdata.txt', 'r')

    line = ''
    ordering = []
    i = 0
    while True:
        line = f.readline()
        if line == '\n':
            break
        ordering.append(line.strip())
    
    pages = []
    while True:
        line = f.readline()
        if line == '' or line == None:
            break
        pages.append(line.strip().split(','))

    return ordering, pages

def create_dictionary(list_of_strings):
    ordering_dictionary = {}
    for s in list_of_strings:
        [before, after] = s.split('|')
        if before not in ordering_dictionary:
            ordering_dictionary[before] = []
        ordering_dictionary[before].append(after)

    return ordering_dictionary

def checkOrdering(ordering, list_of_pages):
    orderedPages = []
    notOrderedPages = []

    for pages in list_of_pages:
        reversedPages = list(reversed(pages))
        ordered = True
        for i,page in enumerate(reversedPages):            
            if page in ordering:
                pageOrder = ordering[page]
                for p in pageOrder:
                    if p in reversedPages[i:]:
                        ordered = False
                        break
            if not ordered:
                break
        if ordered:
            orderedPages.append(pages)
        else:
            notOrderedPages.append(pages)

    return orderedPages, notOrderedPages
            
def fixOrdering(ordering, list_of_pages):
    orderedPages = []
    for pages in list_of_pages:
        newPageOrder = []
        for i, page in enumerate(reversed(pages)):
            inserted = False
            if page in ordering:
                pageOrder = ordering[page]
                for i,p in enumerate(newPageOrder):
                    if p in pageOrder:
                        newPageOrder.insert(i, page)
                        inserted = True
                        break
            if not inserted:
                newPageOrder.append(page)
        orderedPages.append(newPageOrder)
    
    return orderedPages
            

def main():
    ordering, pages = read_file()

    ordering_dict = create_dictionary(ordering)

    #print('------ Pages -----------')
    #for p in pages:
    #   print(p)
    #print('------ Ordering Dict --------')
    #for k,v in ordering_dict.items():
    #    print(f'{k}: {v}')

    orderedPages, notOrderedPages = checkOrdering(ordering_dict, pages)

    print('OK prints')
    #print(orderedPages)
    sum=0
    for op in orderedPages:
        sum += int(op[len(op)//2])
        #print(f'{len(op)} -> {len(op)//2}')
    print(sum)

    print('Not OK prints')
    #for nop in notOrderedPages:
    #    print(nop)

    fixedOrderedPages = fixOrdering(ordering_dict, notOrderedPages)
    #print('Fixed')
    #for fop in fixedOrderedPages:
    #    print(fop)
    sum=0
    for op in fixedOrderedPages:
        sum += int(op[len(op)//2])
    print(sum)

if __name__ == '__main__':
    main()