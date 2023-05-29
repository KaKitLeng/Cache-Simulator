#Author: Ka Kit Leng
#Email: jasonlengkakit@gmail.com
#Assignment: Cache Simulator


# convert hexademical in to binary
def hex_to_binary(str_val):
    # convert the string input into a hex val
    hex_val = int(str_val, base=16)

    # convert the hex value into a bin value and ignore the '0b' infront of the output
    bin_val = bin(hex_val)[2:]
    
    # fill in the bin value with zero until it is 64 bits
    bin_64 = str(bin_val).zfill(64)
    return bin_64


# simulate a cache using 2d list
def cache_creator(s):

    # create a cache using dynamic 2d list
    cache = [[] for j in range(2**s)]

    return cache


# determine if it is a hit, miss, and/or evict
def hit_miss_eviction(s, E, b, cache, address, hit, miss, eviction):

    # convert address into binary
    bin_address = hex_to_binary(address)
    # determine the tag bits
    tag_len = 64 - s - b
    tag_bits = bin_address[0:tag_len]
    # determine set bit
    set_len = tag_len + s
    set_bits = bin_address[tag_len:set_len]
    # determine which set to go to
    set_num = int(set_bits, base=2)

    # search cache
    # if in cache; hit + 1
    if tag_bits in cache[set_num]:
        hit += 1

    # if not in cache and have space, append into cache; miss + 1
    elif tag_bits not in cache[set_num] and len(cache[set_num]) < E:
        cache[set_num].append(tag_bits)
        miss += 1

    # if not in cache and have no space, use FIFO replacement policy;
    # miss + 1, evict + 1
    elif tag_bits not in cache[set_num] and len(cache[set_num]) == E:
        cache[set_num].pop(0)
        cache[set_num].append(tag_bits)
        miss += 1
        eviction += 1
    return hit, miss, eviction


def main():
    hits = 0
    misses = 0
    evictions = 0

    s = int(input("-s Number of set index bits: "))
    E = int(input("-E Associativity (number of lines per set): "))
    b = int(input("-b Number of block bits: "))
    t = input("-t Trace file: ")

    tracefile = open(t, "r")

    # create the cache
    cache = cache_creator(s)

    # read line by line 
    lines = tracefile.readlines()
    for contents in lines:
        # retrive the address. EXP: [" S 10", "1\n"], address is at index[0][3:]
        content = contents.split(",")
        address = content[0][3:]

        # if it is a load(L) or store(S)
        if content[0][1] == "L" or content[0][1] == "S":
            hits, misses, evictions = hit_miss_eviction(s, E, b, cache, address, hits, misses, evictions)
        
        # if it is a modify(M), do both load and store
        elif content[0][1] == "M":
            for i in range(2):
                hits, misses, evictions = hit_miss_eviction(s, E, b, cache,address, hits, misses, evictions)
        
        # if it is an instruction load(I), skip it
        else:
            continue
                
    print("\nhits:", hits, " misses:", misses, " evictions:", evictions)
    
main()

