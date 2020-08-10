i = 0
limit = 1;
while i < limit:
    try: 
        x = input('hi')
    except KeyboardInterrupt:
        limit = limit+1
        continue
    index = index + 1
