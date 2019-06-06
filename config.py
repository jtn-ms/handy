entry_points = [
                # json or txt f handling        
                "handy = handy.cli.cli:main",
                "delkey = handy.cli.json:delKey",
                "rmempty = handy.cli.json:rmEmpty",
                "beautifyjson = handy.cli.json:rmEmpty",
                "chkey = handy.cli.json:chKey",
                "findkey = handy.cli.json:findKey",
                "repl = handy.cli.text:replace",
                "deline = handy.cli.text:deline",
                # git control
                "version = handy.cli.chkinfo:version",
                "commit = handy.cli.git:commit",
                "totalines = handy.cli.text:totalines",
                # frequently-used .bashrc configuration
                "boo = handy.cli.simple:shutdown",
                "cls = handy.cli.simple:clear",
                "bashrc = handy.cli.simple:openbashrc",
                "flush = handy.cli.simple:sourcebashrc",
                "chkbashrc = handy.cli.simple:chkbashrc",
                "upload = handy.cli.transfer:upload",
                "download = handy.cli.transfer:download",
                # encrypt part
                "hash = handy.cli.crypt:hash",
                "encode = handy.cli.crypt:Encode",
                "decode = handy.cli.crypt:Decode",
                "encrypt = handy.cli.crypt:Encrypt",
                "decrypt = handy.cli.crypt:Decrypt",
                # filter
                "column = handy.cli.filter:column",
                "colex = handy.cli.filter:colex",
                "row = handy.cli.filter:row",
                "rowex = handy.cli.filter:rowex",
                "findstr = handy.cli.filter:findstr",
                "extractstr = handy.cli.filter:extractstr",
                "fromstr = handy.cli.filter:fromstr",
                "endstr = handy.cli.filter:endstr",
                "excludestr = handy.cli.filter:excludestr",
                "lenstr = handy.cli.filter:lenstr",
                "upperstr = handy.cli.filter:upperstr",
                "lowerstr = handy.cli.filter:lowerstr",
                "chkstdin = handy.cli.filter:chkstdin",
                # chkinfo
                "dirsize = handy.cli.chkinfo:dirsize",
                "linecount = handy.cli.text:linecount",
                # config
                "replconfkey = handy.cli.config:replconfkey",
                "replconfval = handy.cli.config:replconfval",
                "concatstr = handy.cli.config:concatstr",
                # network
                "mac = handy.cli.chkinfo:mac",
                "pubip = handy.cli.chkinfo:pubip",
                "prvip = handy.cli.chkinfo:privip",
                "gps = handy.cli.chkinfo:gps",
                "ipinfo = handy.cli.chkinfo:ipinfo",
                # clipboard
                #"pbcopy = handy.cli.clipboard:pbcopy",
                #"pbpaste = handy.cli.clipboard:pbpaste",
                # secure
                "srm = handy.cli.secure:srm",
                #
                "genpass = handy.cli.crypt:genpazz",
                # utils
                "timer = handy.cli.utils:timer",
            ]

commands = [cmd.strip().replace(" ",'').split('=')[0] for cmd in entry_points]