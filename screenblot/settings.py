import os

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PHANTOM_BIN = os.path.join(ROOT_PATH, 'bin', 'phantomjs')

TORNADO_SETTINGS = {
    'cookie_secret': ("B_IDxPXx*Oitr p1(SB$@p=m}GbdU?o:ZbvL:=D+zD}@29F{p.bc7O;WC'Zq]Bvv5gxnE|}mojgI#HPL@pi[L._r8[252d~rV(-{)sV^4c4?\P/rVKJ%)3s\[O~2W;uU"),
    'debug': True
}
TORNADO_SERVER_PORT = os.getenv('SCREENBLOT_API_PORT') or 8888
TORNADO_PROCESSES = int(os.getenv('SCREENBLOT_API_PROCESSES')  or 1)
