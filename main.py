from tradingview_ta import *
analysis = get_multiple_analysis(screener="indonesia", interval=Interval.INTERVAL_1_DAY, symbols=[
"idx:goto"
,"idx:AALI"
,"idx:ABBA"
,"idx:ABDA"
,"idx:ABMM"
,"idx:ACES"
,"idx:ACST"
,"idx:ADCP"
,"idx:ADES"
,"idx:ADHI"
,"idx:ADMF"
,"idx:ADMG"
,"idx:ADMR"
,"idx:ADRO"
,"idx:AGAR"
,"idx:AGII"
,"idx:AGRO"
,"idx:AGRS"
,"idx:AHAP"
,"idx:AIMS"
,"idx:AISA"
,"idx:AKKU"
,"idx:AKPI"
,"idx:AKRA"
,"idx:AKSI"
,"idx:ALDO"
,"idx:ALKA"
,"idx:ALMI"
,"idx:ALTO"
,"idx:AMAG"
,"idx:AMAN"
,"idx:AMAR"
,"idx:AMFG"
,"idx:AMIN"
,"idx:AMOR"
,"idx:AMRT"
,"idx:ANDI"
,"idx:ANJT"
,"idx:ANTM"
,"idx:APEX"
,"idx:APIC"
,"idx:APII"
,"idx:APLI"
,"idx:APLN"
,"idx:ARCI"
,"idx:ARGO"
,"idx:ARII"
,"idx:ARKA"
,"idx:ARMY"
,"idx:ARNA"
,"idx:ARTA"
,"idx:ARTI"
,"idx:ARTO"
,"idx:ASBI"
,"idx:ASDM"
,"idx:ASGR"
,"idx:ASHA"
,"idx:ASII"
,"idx:ASJT"
,"idx:ASLC"
,"idx:ASMI"
,"idx:ASPI"
,"idx:ASRI"
,"idx:ASRM"
,"idx:ASSA"
,"idx:ATAP"
,"idx:ATIC"
,"idx:AUTO"
,"idx:AVIA"
,"idx:AYLS"
,"idx:BABP"
,"idx:BACA"
,"idx:BAJA"
,"idx:BALI"
,"idx:BANK"
,"idx:BAPA"
,"idx:BAPI"
,"idx:BATA"
,"idx:BAUT"
,"idx:BAYU"
,"idx:BBCA"
,"idx:BBHI"
,"idx:BBKP"
,"idx:BBLD"
,"idx:BBMD"
,"idx:BBNI"
,"idx:BBRI"
,"idx:BBRM"
,"idx:BBSI"
,"idx:BBSS"
,"idx:BBTN"
,"idx:BBYB"
,"idx:BCAP"
,"idx:BCIC"
,"idx:BCIP"
,"idx:BDMN"
,"idx:BEBS"
,"idx:BEEF"
,"idx:BEKS"
,"idx:BELL"
,"idx:BESS"
,"idx:BEST"
,"idx:BFIN"
,"idx:BGTG"
,"idx:BHAT"
,"idx:BHIT"
,"idx:BIKA"
,"idx:BIKE"
,"idx:BIMA"
,"idx:BINA"
,"idx:BINO"
,"idx:BIPI"
,"idx:BIPP"
,"idx:BIRD"
,"idx:BISI"
,"idx:BJBR"
,"idx:BJTM"
,"idx:BKDP"
,"idx:BKSL"
,"idx:BKSW"
,"idx:BLTA"
,"idx:BLTZ"
,"idx:BLUE"
,"idx:BMAS"
,"idx:BMHS"
,"idx:BMRI"
,"idx:BMSR"
,"idx:BMTR"
,"idx:BNBA"
,"idx:BNBR"
,"idx:BNGA"
,"idx:BNII"
,"idx:BNLI"
,"idx:BOBA"
,"idx:BOGA"
,"idx:BOLA"
,"idx:BOLT"
,"idx:BOSS"
,"idx:BPFI"
,"idx:BPII"
,"idx:BPTR"
,"idx:BRAM"
,"idx:BRIS"
,"idx:BRMS"
,"idx:BRNA"
,"idx:BRPT"
,"idx:BSDE"
,"idx:BSIM"
,"idx:BSML"
,"idx:BSSR"
,"idx:BSWD"
,"idx:BTEK"
,"idx:BTEL"
,"idx:BTON"
,"idx:BTPN"
,"idx:BTPS"
,"idx:BUDI"
,"idx:BUKA"
,"idx:BUKK"
,"idx:BULL"
,"idx:BUMI"
,"idx:BUVA"
,"idx:BVIC"
,"idx:BWPT"
,"idx:BYAN"
,"idx:CAKK"
,"idx:CAMP"
,"idx:CANI"
,"idx:CARE"
,"idx:CARS"
,"idx:CASA"
,"idx:CASH"
,"idx:CASS"
,"idx:CBMF"
,"idx:CCSI"
,"idx:CEKA"
,"idx:CENT"
,"idx:CFIN"
,"idx:CINT"
,"idx:CITA"
,"idx:CITY"
,"idx:CLAY"
,"idx:CLEO"
,"idx:CLPI"
,"idx:CMNP"
,"idx:CMNT"
,"idx:CMPP"
,"idx:CMRY"
,"idx:CNKO"
,"idx:CNTB"
,"idx:CNTX"
,"idx:COCO"
,"idx:COWL"
,"idx:CPIN"
,"idx:CPRI"
,"idx:CPRO"
,"idx:CSAP"
,"idx:CSIS"
,"idx:CSMI"
,"idx:CSRA"
,"idx:CTBN"
,"idx:CTRA"
,"idx:CTTH"
,"idx:DADA"
,"idx:DART"
,"idx:DAYA"
,"idx:DCII"
,"idx:DEAL"
,"idx:DEFI"
,"idx:DEPO"
,"idx:DEWA"
,"idx:DFAM"
,"idx:DGIK"
,"idx:DGNS"
,"idx:DIGI"
,"idx:DILD"
,"idx:DIVA"
,"idx:DKFT"
,"idx:DLTA"
,"idx:DMAS"
,"idx:DMMX"
,"idx:DMND"
,"idx:DNAR"
,"idx:DNET"
,"idx:DOID"
,"idx:DPNS"
,"idx:DPUM"
,"idx:DRMA"
,"idx:DSFI"
,"idx:DSNG"
,"idx:DSSA"
,"idx:DUCK"
,"idx:DUTI"
,"idx:DVLA"
,"idx:DWGL"
,"idx:DYAN"
,"idx:EAST"
,"idx:ECII"
,"idx:EDGE"
,"idx:EKAD"
,"idx:ELSA"
,"idx:ELTY"
,"idx:EMDE"
,"idx:EMTK"
,"idx:ENAK"
,"idx:ENRG"
,"idx:ENVY"
,"idx:ENZO"
,"idx:EPAC"
,"idx:EPMT"
,"idx:ERAA"
,"idx:ERTX"
,"idx:ESIP"
,"idx:ESSA"
,"idx:ESTA"
,"idx:ESTI"
,"idx:ETWA"
,"idx:EXCL"
,"idx:FAPA"
,"idx:FAST"
,"idx:FASW"
,"idx:FILM"
,"idx:FIMP"
,"idx:FIRE"
,"idx:FISH"
,"idx:FITT"
,"idx:FLMC"
,"idx:FMII"
,"idx:FOOD"
,"idx:FORU"
,"idx:FORZ"
,"idx:FPNI"
,"idx:FREN"
,"idx:FUJI"
,"idx:GAMA"
,"idx:GDST"
,"idx:GDYR"
,"idx:GEMA"
,"idx:GEMS"
,"idx:GGRM"
,"idx:GGRP"
,"idx:GHON"
,"idx:GIAA"
,"idx:GJTL"
,"idx:GLOB"
,"idx:GLVA"
,"idx:GMFI"
,"idx:GMTD"
,"idx:GOLD"
,"idx:GOLL"
,"idx:GOOD"
,"idx:GPRA"
,"idx:GPSO"
,"idx:GSMF"
,"idx:GTBO"
,"idx:GTSI"
,"idx:GWSA"
,"idx:GZCO"
,"idx:HADE"
,"idx:HAIS"
,"idx:HDFA"
,"idx:HDIT"
,"idx:HDTX"
,"idx:HEAL"
,"idx:HELI"
,"idx:HERO"
,"idx:HEXA"
,"idx:HITS"
,"idx:HKMU"
,"idx:HMSP"
,"idx:HOKI"
,"idx:HOME"
,"idx:HOMI"
,"idx:HOPE"
,"idx:HOTL"
,"idx:HRME"
,"idx:HRTA"
,"idx:HRUM"
,"idx:IATA"
,"idx:IBFN"
,"idx:IBOS"
,"idx:IBST"
,"idx:ICBP"
,"idx:ICON"
,"idx:IDEA"
,"idx:IDPR"
,"idx:IFII"
,"idx:IFSH"
,"idx:IGAR"
,"idx:IIKP"
,"idx:IKAI"
,"idx:IKAN"
,"idx:IKBI"
,"idx:IMAS"
,"idx:IMJS"
,"idx:IMPC"
,"idx:INAF"
,"idx:INAI"
,"idx:INCF"
,"idx:INCI"
,"idx:INCO"
,"idx:INDF"
,"idx:INDO"
,"idx:INDR"
,"idx:INDS"
,"idx:INDX"
,"idx:INDY"
,"idx:INKP"
,"idx:INOV"
,"idx:INPC"
,"idx:INPP"
,"idx:INPS"
,"idx:INRU"
,"idx:INTA"
,"idx:INTD"
,"idx:INTP"
,"idx:IPAC"
,"idx:IPCC"
,"idx:IPCM"
,"idx:IPOL"
,"idx:IPPE"
,"idx:IPTV"
,"idx:IRRA"
,"idx:ISAT"
,"idx:ISSP"
,"idx:ITIC"
,"idx:ITMA"
,"idx:ITMG"
,"idx:JAST"
,"idx:JAWA"
,"idx:JAYA"
,"idx:JECC"
,"idx:JGLE"
,"idx:JIHD"
,"idx:JKON"
,"idx:JKSW"
,"idx:JMAS"
,"idx:JPFA"
,"idx:JRPT"
,"idx:JSKY"
,"idx:JSMR"
,"idx:JSPT"
,"idx:JTPE"
,"idx:KAEF"
,"idx:KARW"
,"idx:KAYU"
,"idx:KBAG"
,"idx:KBLI"
,"idx:KBLM"
,"idx:KBLV"
,"idx:KBRI"
,"idx:KDSI"
,"idx:KEEN"
,"idx:KEJU"
,"idx:KIAS"
,"idx:KICI"
,"idx:KIJA"
,"idx:KINO"
,"idx:KIOS"
,"idx:KJEN"
,"idx:KKGI"
,"idx:KLBF"
,"idx:KMDS"
,"idx:KMTR"
,"idx:KOBX"
,"idx:KOIN"
,"idx:KONI"
,"idx:KOPI"
,"idx:KOTA"
,"idx:KPAL"
,"idx:KPAS"
,"idx:KPIG"
,"idx:KRAH"
,"idx:KRAS"
,"idx:KREN"
,"idx:KUAS"
,"idx:LABA"
,"idx:LAND"
,"idx:LAPD"
,"idx:LCGP"
,"idx:LCKM"
,"idx:LEAD"
,"idx:LFLO"
,"idx:LIFE"
,"idx:LINK"
,"idx:LION"
,"idx:LMAS"
,"idx:LMPI"
,"idx:LMSH"
,"idx:LPCK"
,"idx:LPGI"
,"idx:LPIN"
,"idx:LPKR"
,"idx:LPLI"
,"idx:LPPF"
,"idx:LPPS"
,"idx:LRNA"
,"idx:LSIP"
,"idx:LTLS"
,"idx:LUCK"
,"idx:LUCY"
,"idx:MABA"
,"idx:MAGP"
,"idx:MAIN"
,"idx:MAMI"
,"idx:MAMIP"
,"idx:MAPA"
,"idx:MAPB"
,"idx:MAPI"
,"idx:MARI"
,"idx:MARK"
,"idx:MASA"
,"idx:MASB"
,"idx:MAYA"
,"idx:MBAP"
,"idx:MBSS"
,"idx:MBTO"
,"idx:MCAS"
,"idx:MCOL"
,"idx:MCOR"
,"idx:MDIA"
,"idx:MDKA"
,"idx:MDKI"
,"idx:MDLN"
,"idx:MDRN"
,"idx:MEDC"
,"idx:MEGA"
,"idx:MERK"
,"idx:META"
,"idx:MFIN"
,"idx:MFMI"
,"idx:MGLV"
,"idx:MGNA"
,"idx:MGRO"
,"idx:MICE"
,"idx:MIDI"
,"idx:MIKA"
,"idx:MINA"
,"idx:MIRA"
,"idx:MITI"
,"idx:MKNT"
,"idx:MKPI"
,"idx:MLBI"
,"idx:MLIA"
,"idx:MLPL"
,"idx:MLPT"
,"idx:MMLP"
,"idx:MNCN"
,"idx:MOLI"
,"idx:MPMX"
,"idx:MPOW"
,"idx:MPPA"
,"idx:MPRO"
,"idx:MRAT"
,"idx:MREI"
,"idx:MSIN"
,"idx:MSKY"
,"idx:MTDL"
,"idx:MTEL"
,"idx:MTFN"
,"idx:MTLA"
,"idx:MTMH"
,"idx:MTPS"
,"idx:MTRA"
,"idx:MTSM"
,"idx:MTWI"
,"idx:MYOH"
,"idx:MYOR"
,"idx:MYRX"
,"idx:MYRXP"
,"idx:MYTX"
,"idx:NANO"
,"idx:NASA"
,"idx:NASI"
,"idx:NATO"
,"idx:NELY"
,"idx:NETV"
,"idx:NFCX"
,"idx:NICK"
,"idx:NICL"
,"idx:NIKL"
,"idx:NIPS"
,"idx:NIRO"
,"idx:NISP"
,"idx:NOBU"
,"idx:NPGF"
,"idx:NRCA"
,"idx:NTBK"
,"idx:NUSA"
,"idx:NZIA"
,"idx:OASA"
,"idx:OBMD"
,"idx:OCAP"
,"idx:OILS"
,"idx:OKAS"
,"idx:OLIV"
,"idx:OMRE"
,"idx:OPMS"
,"idx:PADI"
,"idx:PALM"
,"idx:PAMG"
,"idx:PANI"
,"idx:PANR"
,"idx:PANS"
,"idx:PBID"
,"idx:PBRX"
,"idx:PBSA"
,"idx:PCAR"
,"idx:PDES"
,"idx:PEGE"
,"idx:PEHA"
,"idx:PGAS"
,"idx:PGJO"
,"idx:PGLI"
,"idx:PGUN"
,"idx:PICO"
,"idx:PJAA"
,"idx:PKPK"
,"idx:PLAN"
,"idx:PLAS"
,"idx:PLIN"
,"idx:PMJS"
,"idx:PMMP"
,"idx:PNBN"
,"idx:PNBS"
,"idx:PNGO"
,"idx:PNIN"
,"idx:PNLF"
,"idx:PNSE"
,"idx:POLA"
,"idx:POLI"
,"idx:POLL"
,"idx:POLU"
,"idx:POLY"
,"idx:POOL"
,"idx:PORT"
,"idx:POSA"
,"idx:POWR"
,"idx:PPGL"
,"idx:PPRE"
,"idx:PPRO"
,"idx:PRAS"
,"idx:PRDA"
,"idx:PRIM"
,"idx:PSAB"
,"idx:PSDN"
,"idx:PSGO"
,"idx:PSKT"
,"idx:PSSI"
,"idx:PTBA"
,"idx:PTDU"
,"idx:PTIS"
,"idx:PTPP"
,"idx:PTPW"
,"idx:PTRO"
,"idx:PTSN"
,"idx:PTSP"
,"idx:PUDP"
,"idx:PURA"
,"idx:PURE"
,"idx:PURI"
,"idx:PWON"
,"idx:PYFA"
,"idx:PZZA"
,"idx:RAJA"
,"idx:RALS"
,"idx:RANC"
,"idx:RBMS"
,"idx:RDTX"
,"idx:REAL"
,"idx:RELI"
,"idx:RICY"
,"idx:RIGS"
,"idx:RIMO"
,"idx:RISE"
,"idx:RMBA"
,"idx:RMKE"
,"idx:ROCK"
,"idx:RODA"
,"idx:RONY"
,"idx:ROTI"
,"idx:RSGK"
,"idx:RUIS"
,"idx:RUNS"
,"idx:SAFE"
,"idx:SAME"
,"idx:SAMF"
,"idx:SAPX"
,"idx:SATU"
,"idx:SBAT"
,"idx:SBMA"
,"idx:SCCO"
,"idx:SCMA"
,"idx:SCNP"
,"idx:SCPI"
,"idx:SDMU"
,"idx:SDPC"
,"idx:SDRA"
,"idx:SEMA"
,"idx:SFAN"
,"idx:SGER"
,"idx:SGRO"
,"idx:SHID"
,"idx:SHIP"
,"idx:SICO"
,"idx:SIDO"
,"idx:SILO"
,"idx:SIMA"
,"idx:SIMP"
,"idx:SINI"
,"idx:SIPD"
,"idx:SKBM"
,"idx:SKLT"
,"idx:SKRN"
,"idx:SKYB"
,"idx:SLIS"
,"idx:SMAR"
,"idx:SMBR"
,"idx:SMCB"
,"idx:SMDM"
,"idx:SMDR"
,"idx:SMGR"
,"idx:SMKL"
,"idx:SMKM"
,"idx:SMMA"
,"idx:SMMT"
,"idx:SMRA"
,"idx:SMRU"
,"idx:SMSM"
,"idx:SNLK"
,"idx:SOCI"
,"idx:SOFA"
,"idx:SOHO"
,"idx:SONA"
,"idx:SOSS"
,"idx:SOTS"
,"idx:SPMA"
,"idx:SPTO"
,"idx:SQMI"
,"idx:SRAJ"
,"idx:SRIL"
,"idx:SRSN"
,"idx:SRTG"
,"idx:SSIA"
,"idx:SSMS"
,"idx:SSTM"
,"idx:STAA"
,"idx:STAR"
,"idx:STTP"
,"idx:SUGI"
,"idx:SULI"
,"idx:SUPR"
,"idx:SURE"
,"idx:SWAT"
,"idx:TALF"
,"idx:TAMA"
,"idx:TAMU"
,"idx:TAPG"
,"idx:TARA"
,"idx:TAXI"
,"idx:TAYS"
,"idx:TBIG"
,"idx:TBLA"
,"idx:TBMS"
,"idx:TCID"
,"idx:TCPI"
,"idx:TDPM"
,"idx:TEBE"
,"idx:TECH"
,"idx:TELE"
,"idx:TFAS"
,"idx:TFCO"
,"idx:TGKA"
,"idx:TGRA"
,"idx:TIFA"
,"idx:TINS"
,"idx:TIRA"
,"idx:TIRT"
,"idx:TKIM"
,"idx:TLDN"
,"idx:TLKM"
,"idx:TMAS"
,"idx:TMPO"
,"idx:TNCA"
,"idx:TOBA"
,"idx:TOPS"
,"idx:TOTL"
,"idx:TOTO"
,"idx:TOWR"
,"idx:TOYS"
,"idx:TPIA"
,"idx:TPMA"
,"idx:TRAM"
,"idx:TRIL"
,"idx:TRIM"
,"idx:TRIN"
,"idx:TRIO"
,"idx:TRIS"
,"idx:TRJA"
,"idx:TRST"
,"idx:TRUE"
,"idx:TRUK"
,"idx:TRUS"
,"idx:TSPC"
,"idx:TUGU"
,"idx:TURI"
,"idx:UANG"
,"idx:UCID"
,"idx:UFOE"
,"idx:ULTJ"
,"idx:UNIC"
,"idx:UNIQ"
,"idx:UNIT"
,"idx:UNSP"
,"idx:UNTR"
,"idx:UNVR"
,"idx:URBN"
,"idx:UVCR"
,"idx:VICI"
,"idx:VICO"
,"idx:VINS"
,"idx:VIVA"
,"idx:VOKS"
,"idx:VRNA"
,"idx:WAPO"
,"idx:WEGE"
,"idx:WEHA"
,"idx:WGSH"
,"idx:WICO"
,"idx:WIFI"
,"idx:WIIM"
,"idx:WIKA"
,"idx:WINR"
,"idx:WINS"
,"idx:WIRG"
,"idx:WMPP"
,"idx:WMUU"
,"idx:WOMF"
,"idx:WOOD"
,"idx:WOWS"
,"idx:WSBP"
,"idx:WSKT"
,"idx:WTON"
,"idx:YELO"
,"idx:YPAS"
,"idx:YULE"
,"idx:ZBRA"
,"idx:ZINC"
,"idx:ZONE"
,"idx:ZYRX" 
])

for key, value in analysis.items():
    if value!='None' and value.summary["RECOMMENDATION"]=='BUY':
        print(key, ' : ', value.summary)



#print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}