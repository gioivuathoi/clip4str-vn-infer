from editdistance import eval
from dict_trie import Trie

def gen_candidate(dictionary:list, trie:Trie, rec:str, num_samples:int = 150, dis = 1):
    if len(rec) == 0:
      return []
    candidates_list = list(trie.all_levenshtein(rec.lower(), dis))
    # new_dis = dis
    # while len(candidates_list) == 0:
    #   new_dis = new_dis + 1
    #   if new_dis == 4:
    #     return candidates_list
    #   candidates_list = list(trie.all_levenshtein(rec.lower(), new_dis))
    if len(candidates_list) == 0:
      return []
    if rec.isupper():
      for i,cand in enumerate(candidates_list):
        candidates_list[i] = candidates_list[i].upper()
    elif rec[0].isupper():
      for i,cand in enumerate(candidates_list):
          cand = cand.lower()
          if len(cand) == 0:
            continue
          if len(cand) == 1:
            cand = cand.upper()
          else:
            cand = cand[0].upper() + cand[1:]
          candidates_list[i] = cand
    # else:
    #     for i,cand in enumerate(candidates_list):
    #         cand = cand.lower()
    #         candidates_list[i] = cand
    final = []
    for cand in candidates_list:
      if cand not in final and cand != "":
        final.append(cand)
    if len(final) > num_samples:
        return final[:num_samples]
    else:
        return final
#Should return a list of "num_sample" candidates
    
if __name__ == "__main__":
    dictionary = open("/content/drive/MyDrive/clip4str/code/clip4str/strhub/data/syllables.txt").read().replace("\n\n", "\n").split("\n")
    print("Number of word in dictionary: ", dictionary)
    trie = Trie(dictionary)
    rec = "BRIIAD"
    candidates_list = list(trie.all_levenshtein(rec, 2))
    print(candidates_list)
