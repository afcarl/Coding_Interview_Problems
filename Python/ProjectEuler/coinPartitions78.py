'''
Created on Sep 22, 2014

@author: Ben Athiwaratkun (pa338)

'''

def coinPartitions(maxNumCoins, multiplier):
    _table = []
    _table.append([1])
    while(len(_table) < maxNumCoins or not ( (_table[-1][-1] % multiplier) == 0)  ):
        numCoins = len(_table) + 1
        row = [0]*numCoins
        for bound in range(1, numCoins+1):
            for sizeFirst in range(1, bound+1):
                if sizeFirst < bound:
                    coinLeft = numCoins - sizeFirst
                    #print "numCoins", numCoins
                    #print "sizeFirst", sizeFirst
                    #print "coinLeft-1:", (coinLeft-1)
                    #print "bound-1:", (bound-1)
                    #theBound = min(bound-1,coinLeft-1)
                    theBound = min(sizeFirst-1, coinLeft-1)
                    row[bound-1] += _table[coinLeft-1][theBound]
                else:
                    row[bound-1] += 1
        _table.append(row)
        
        print "Iteration ", len(_table)
        #print _table
    return (numCoins, _table[numCoins-1][numCoins-1])
# come up with a faster algorithm    

def main():
    pair  = coinPartitions(6,1)
    print "(Number of coins, number of ways to group)", pair
    
if __name__ == "__main__":
    main()