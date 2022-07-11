
Jak zacząć
===========

W tej sekcji zostanie opisane co jest potrzebne do uruchomienia aplikacji i jak jej używać

Potrzebne biblioteki
--------------------

Należy mieć:

- Python w wersji 3.8 lub nowszy, preferowana dystrubujca Anaconda
- Zainstalowane paczki z repozytorium pip określone w pliku **requirements.txt**

paczki można łatwo zainstalować używając komendy:

.. code-block:: shell

    python3 -m pip install -r requirements.txt

Jak uruchomić aplikację
---------

Training the model
..................

.. code-block:: shell

    python3 wavenet_tts.py train --config [config_path]

Generating audio from text
.........................

.. code-block:: shell

    python3 wavenet_tts.py generate --config [config_path] --out [audio_out_path]

For providing text there are 3 ways:

- using `--text` option from command e.g.

.. code-block:: shell

    python3 wavenet_tts.py generate --text "some funny text" ...rest


- inputing from console after running the app, app will ask for input
- using terminal pipe functionality e.g.

.. code-block:: shell

    cat some_file_with_text.txt | python3 wavenet_tts_main.py ...rest

Przykładowe zestwy danych
----------------------

- LJSpeech_ Dataset_

.. _LJSpeech: https://keithito.com/LJ-Speech-Dataset/

__ LJSpeech_

.. _Dataset: https://keithito.com/LJ-Speech-Dataset/

__ Dataset_

