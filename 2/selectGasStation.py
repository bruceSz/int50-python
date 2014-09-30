
# gasArr stores gas in #gasStation,
# costArr stores #consumeGas from index 'i' to 'i+1'
def selectGasStation(gasArr, costArr):
    curr_gas = 0
    curr_cost = 0
    start = 0
    end = 1
    length = 1
    #for index,gas in enumerate(gasArr):
    while length < len(gasArr)

        curr_gas += gas
        curr_cost += costArr
        if curr_gas< curr_cost:
            while curr_gas<curr_cost:
                curr_gas -= gasArr[start]
                curr_cost -= costArr[start]

                start += 1
                start = (start%len(gasArr))
                length -= 1

                if start == end:
                    end += 1
                    end = (end%len(gasArr))
                    length = 1
        else:
            end += 1
            end = (end%len(gasArr))
            length += 1

    return start

