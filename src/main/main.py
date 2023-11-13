from configHandler import Configuration



def __main__():
    conf = Configuration(r"example/a.hwk")
    conf.load()
    print(conf.last_modified)    
    return 0


if __main__:
    print('\n'*3+'*'*20+f"\nexit status {__main__()}")