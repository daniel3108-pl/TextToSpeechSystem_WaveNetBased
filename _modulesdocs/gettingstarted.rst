
Jak zacząć
===========

W tej sekcji zostanie opisane co jest potrzebne do uruchomienia aplikacji i jak jej używać.

Potrzebne biblioteki
--------------------

Należy mieć:

- Python w wersji 3.8 lub nowszy, preferowana dystrubujca Anaconda
- Zainstalowane paczki z repozytorium pip określone w pliku **requirements.txt**
- Preferowane są systemy Linux lub macOS, wszystkie pomoce są prezentowane w tych systemach, jednak aplikacja powinna się uruchamiać na systemach Windows poprawnie

paczki można łatwo zainstalować używając komendy:

.. code-block:: shell

    python3 -m pip install -r requirements.txt

Jak uruchomić aplikację
---------

Trenowanie modelu
..................

.. code-block:: shell

    python3 wavenet_tts.py train --config [config_path]

Generowanie audio z tekstu
.........................

.. code-block:: shell

    python3 wavenet_tts.py generate --config [config_path] --out [audio_out_path]

By podać tekst, z którego chcemy wygenerować możemy użyć 3 sposobów:

- użycie argumentu `--text` w komendzie np.

.. code-block:: shell

    python3 wavenet_tts.py generate --text "some funny text" ...rest


- podanie tekstu gdy aplikacja zapyta nas o to
- użycie funkcji potoku w terminalu bash np.

.. code-block:: shell

    cat some_file_with_text.txt | python3 wavenet_tts_main.py ...rest

Argumenty aplikacji i okienka pomocy
---------

Aby uzyskać pomoc dla każdego z modułów aplikacji piszemy

.. code-block:: shell

    python3 wavenet_tts.py --help

Wynik zapytania dla całego programu:
...

.. code-block:: shell

    usage: wavenet_tts.py [-h] {train,generate} ...

    positional arguments:
      {train,generate}  Choose program functionality [training model | generating audio from text], You can use [--help | -h] with each command to see its arguments
        train           Using it will make program train your model
        generate        Using it will make program generate audio based on your input

    optional arguments:
      -h, --help        show this help message and exit

Wynik zapytania help dla modułu trenującego:
....

Komenda:

.. code-block:: shell

    python3 wavenet_tts.py train --help

Wynik:

.. code-block:: shell

    usage: wavenet_tts.py train [-h] [--config CONFIG]

    optional arguments:
      -h, --help       show this help message and exit
      --config CONFIG  Set optional config file to your training process

Wynik zapytania help dla modułu generującego audio:
.....

Komenda:

.. code-block:: shell

    python3 wavenet_tts.py generate --help

Wynik:

.. code-block:: shell

    usage: wavenet_tts.py generate [-h] [--config CONFIG] [--out OUT_FILE] [--text TEXT]

    optional arguments:
      -h, --help       show this help message and exit
      --config CONFIG  Set optional config file to your generating process
      --out OUT_FILE   Name of output file
      --text TEXT      Text to generate audio from

Przykładowe pliki configuracyjne:
-----------------------

Pliki konfiguracyjne tworzymy używając standardu yaml. Poniżej przedstawione zostaną przykładowe
pliki konfiguracyjne dla każdego z modułów aplikacji.


Konfiguracja trenowania:
............

.. code-block:: yaml

    # Przykładowy plik Konfiguracyjny do trenowania modelu
    #
    model:                              # Konfiguracja parameterów uczenia
      encoder:                          # konfiguracja dla encodera
        epochs: 20
        batch-size: 10
        learning-rate: 0.01
      decoder:                          # konfiguracja dla decodera
        epochs: 20
        batch-size: 10
        learning-rate: 0.01
      wavenet:                          # konfiguracja dla wavenetu
        epochs: 20
        batch-size: 10
        learning-rate: 0.01
      output-file: out.pth
    dataset:                            # Konfiguracja zestawu danych uczących
      root-dir: ./dataset/
      definition-file: metadata.csv       # csv z opisem i powiązaniem wypowiedzi tekstowych z plikami csv
      audio-directory: wavs/         # ścieżka do plików audio w kontekscie root-dir np. root-dir/sciezka

Konfiguracja generowania mowy:
........

.. code-block:: yaml

    model-file: some_path/model.pth
    audio-format: wav
    output-dir: someout/
    output-file: somename

Przygotowania zestawu danych do trenowania:
----------------------

Przygotowany zestaw danych powinien być w archiwum podany jako archiwum .zip lub jako struktura katalogów.

Zarówno struktura jaki plik zip powinny prezentować taką hierarchię:

.. code-block::

    dataset
    ├── README
    ├── metadata.csv
    └── wavs/

(Plik README jest nie potrzebny)

Plik metadata.csv posiada 3 kolumny, pierwsza z nazwą pliku wav, druga z wypowiedzią z zachowanymi znakami specjlanymi, trzecia bez znaków specjalnych a liczby prezentowane jako słowa
Katalog wavs/ przechowuje odpowiadające dla pliku csv pliki audio.

Nazewnictwo katalogów i pliku csv jest dowolne przyczym należy je odpowiednio opisać w pliku konfiguracyjnym.

W przypadku gdy korzystamy z pliku zip, root-dir w konfiguracji jest podawana ścieżka pliku zip.
W przypadku użycia katalogu oznacza on ktalog z o struktórze prezentowanej powyżej.

Przykładowe zestwy danych
----------------------

- `LJSpeech Dataset`_

.. _LJSpeech Dataset: https://keithito.com/LJ-Speech-Dataset/

Zestaw ten jest używany w celu prezentacji działania

