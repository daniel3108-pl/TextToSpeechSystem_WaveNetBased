
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

Przykładowe zestwy danych
----------------------

- `LJSpeech Dataset`_

.. _LJSpeech Dataset: https://keithito.com/LJ-Speech-Dataset/

Zestaw ten jest używany w celu prezentacji działania

