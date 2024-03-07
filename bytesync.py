from source import __args__ as _args

args=_args.args().return_args()
logo="""\
██████  ██    ██ ████████ ███████ ███████ ██    ██ ███    ██  ██████ 
██   ██  ██  ██     ██    ██      ██       ██  ██  ████   ██ ██      
██████    ████      ██    █████   ███████   ████   ██ ██  ██ ██      
██   ██    ██       ██    ██           ██    ██    ██  ██ ██ ██      
██████     ██       ██    ███████ ███████    ██    ██   ████  ██████ 
                                                                                                                                       
"""
print(logo)
if args.listen:
    from source import listen
    l=listen.listen(args.host, int(args.port))
    l.listen(args.outfile)
if args.transmit:
    from source import transmit
    t=transmit.transmit(args.host, int(args.port))
    t.transmit(args.file)