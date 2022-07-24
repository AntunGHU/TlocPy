# 14'17 CoryShaffer

# Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module
# osnovno je da u env daje python verziju s kojom je env i izgradjen!
# ? python3 -m venv project_env
# ? source project_env/bin/activate     # (project_env)
# ? pip list        # jednom u env vise ne moramo stavljati brojke pokraj pip i python
# ? pip install requests
# ? pip freeze > requirements.txt
# ? cat requirements.txt
# ? deactivate

# ako nam vise netreba brisemo mapu
# ? rm -rf project_env/

# opce:
# obicno env-mapu stavlja unutar projekta i obicno joj daje ime "venv" ali ne stavlja fajlove projekta u venv! (venv mapa je i mora ostati nesto sto se moze baciti i rebuild-ati) a niti komita mapu venv git-u!! Jedino se git-u komita "requirements.txt" kojim useri mogu rebuldati environment!!
# ? mkdir my_project
# ? python3 -m venv my_project/venv
# ? source my_project/venv/bin/activate

# nakon aktiviranja env-a ako zelimo iskoristiti "requirements.txt" i instalirati sve (req..txt mora biti u root-folderu pr)
# ? pip install -r requirements.txt # ako je u istom dir-u

# ako zelimo pri kreiranju povezati venv sa globalnim paketima (upitno koje ce onda freeze ukljuciti i sam cory kaze da to ne radi) koristimo k-du
# ? source project_env/bin/activate --system-site-packages        # (project_env)
# svi paketi koji se poslije instaliraju su samo lokalni sto pokazuje k-da
# ? pip list --local
# a i freeze ce samo te dodatne izlistati!!
# ? pip freeze --local
