import random

# LARGE PRIME NUMBERS
large_primes = \
    [35201546659608842026088328007565866231962578784643756647773109869245232364730066609837018108561065242031153677,
     10513733234846849736873637829838635104309714688896631127438692162131857778044158273164093838937083421380041997,
     24684249032065892333066123534168930441269525239006410135714283699648991959894332868446109170827166448301044689,
     76921421106760125285550929240903354966370431827792714920086011488103952094969175731459908117375995349245839343,
     32998886283809577512914881459957314326750856532546837122557861905096711274255431870995137546575954361422085081,
     30925729459015376480470394633122420870296099995740154747268426836472045107181955644451858184784072167623952123,
     14083359469338511572632447718747493405040362318205860500297736061630222431052998057250747900577940212317413063,
     10422980533212493227764163121880874101060283221003967986026457372472702684601194916229693974417851408689550781,
     36261430139487433507414165833468680972181038593593271409697364115931523786727274410257181186996611100786935727,
     15579763548573297857414066649875054392128789371879472432457450095645164702139048181789700140949438093329334293,
     499490918065850301921197603564081112780623690273420984342968690594064612108591217229304461006005170865294466527 /
     166368851, 5276540886461085403629823900440198638525533817568390647395895077673310897832541997323026747184971251 /
     24586822562788766953, 17198921883247087085792370174278085041937347517504379537560767604779251731156633921754375 /
     4147263751973899368604441353849, 566039327581077714561506815784669881914684785030580378761402844355426865405282 /
     719619236551816895924694614829004713040283, 8975039575042274721394841994300660103381393431631454192801833142910 /
     67450988520718807102741476596034735471026312154231263, 74521369819173700363131969475312542929396816600297053793 /
     6165661845575001172678049743806549549977234670072449443569701103, 420145406901811857791227072284165226561693483 /
     222287527567496017033892563342686752247587935117119306171161848593337649107, 3711324720881732097411531849817427 /
     71278849120163424101995797949338636074962048027958518451774716413729510755717494155299, 28456374401544054744907 /
     6942566482643882733461003510727231069524112903402006758875891142531990667183056335233985448160393]


def fast_exponentiation(a, b, n):
    if b == 0:
        return 1 if a else 0
    temp = fast_exponentiation(a, b // 2, n)
    return ((temp * temp) % n * a) % n if b & 1 else (temp * temp) % n


if __name__ == '__main__':
    p = large_primes[random.randint(0, len(large_primes) - 1)]
    alpha = random.randint(20, 50)
    print("DOMAIN PARAMETERS:\nAlpha: {}\tP: {}".format(alpha, p))
    a, b = random.randint(2, p - 2), random.randint(2, p - 2)  # Always choose from the Cyclic group Z*(p) : [2, p - 2]
    public_key_A, public_key_B = fast_exponentiation(alpha, a, p), fast_exponentiation(alpha, b, p)
    private_key_A, private_key_B = fast_exponentiation(public_key_B, a, p), fast_exponentiation(public_key_A, b, p)
    print("PROOF OF CORRECTNESS:\nPrivate key generated by A: {}\nPrivate key generated by B: {}".format(private_key_A,
                                                                                                         private_key_B))
    print("Difference: {}".format(private_key_B - private_key_A))
    print("PUBLIC KEYS:\nA: {}\tB: {}".format(public_key_A, public_key_B))
    print("PRIVATE KEY:\n{}".format(private_key_A))
