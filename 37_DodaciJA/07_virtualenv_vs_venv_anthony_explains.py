# 11'21

# * venv
# ? virtualenv
# ! venv na Win
# ante stavio 2 terma i paralelno pokazuje kako s virtualenv tj venv. Globalno, venv je stvar nastala sa python3.3 dok je v-env stariji jos od py2. v-env je brzi i moze mjenjati verzije u env a venv ne moze

# nacili kako vidjeti sto sve ulazi u globalnu instalaciju python-a koja dolazi sa ubuntu 2004 kdom:
# ? dpkg - l | python3-
# sto izbacuje vrlo dugacak spisak, dole na kraju kojeg ipšak necu staviti

# kreiranje env-a
# podrazumjeva se da to radimo sa termom unutar mape projekta i da smo prethodno vec instalirali "virtualenv" paket
# ? virtualenv venv1
# * python3 -m venv venv2
# ! python -m venv venvw    # kde u cmd-eu ili powershell-u

# aktiviranje env-a
# ? source venv1/bin/activate    # (venv1) antun@ub:~/adev$
# ? echo $VIRTUAL_ENV    # /home/antun/adev/venv1
# ? echo $PATH   # /home/antun/adev/venv1/bin:/home/antun/.local/bin:/home/antun/bin:/usr/l
# ? which python   # /home/antun/adev/venv1/bin/python
# * source venv2/bin/activate    # (venv2) antun@ub:~/adev$
# * echo, which isto samo bi bio venv2
# ! venvw\Scripts\activate  # (venvw) C:\Users\Antun\adev>
# ! echo %PATH%     # C:\Users\Antun\adev\venvw\Scripts; C:\Program files... itd isto kao lx-a

# instaliranje paketa u venv-ove
# ? (venv1) antun@ub:~/adev$ pip install pre-commit  # ide sve u venv1
# * sve isto
# ! isto

# razlike i zasto ante preferira virtualenv
# ? minus: mora se posebni instalirati a venv dolazi u py-u (poneka i ne pa seu debian i ubuntu mora instalirati)
# ? radi i sa py2 dok venv samo sa py3.3+
# ? v-env dopusta dok venv ne dopusta mjenjanje verzije tj ako globaly run-amo 3.8 i u env mozemo imati samo 3.8
# ? k-da za kreiranje proizvoljne verzije (venv310) env-a sa virtualenv
# virtualenv venv310 -p python3.10
