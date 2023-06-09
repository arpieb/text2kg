# text2kg
Quick-n-Dirty&trade; text-to-knowledge-graph PoC using off-the-shelf tooling, inspired by approach + code in [mdipietro09/DataScience_ArtificialIntelligence_Utils](https://github.com/mdipietro09/DataScience_ArtificialIntelligence_Utils).

YMMV; this PoC was born from explorations into using KGs to construct fine-tuning datasets for instruct-oriented LLMs based on approaches proposed in [this article](https://betterprogramming.pub/large-language-model-knowledge-graph-store-yes-by-fine-tuning-llm-with-kg-f88b556959e6).

## Installation

Yah, yah, I know I should have packaged this into something installable.  It did start life as a PoC after all...

```bash
# Example install using virtualenv + pip in bash
python3 -m venv ENV
. ENV/bin/activate
pip install --upgrade pip wheel # optional; good housekeeping
pip install -r requirements.py3
```

## Example

- Load up the raw text version of [RFC-1](https://www.rfc-editor.org/rfc/rfc1)
- Construct a knowledge graph from the corpus (returned as NetworkX DiGraph)
- Visualize the KG

```python
import urllib.request
from text2kg import text2kg, plot_kg

text = urllib.request.urlopen('https://www.rfc-editor.org/rfc/rfc1.txt') \
    .read() \
    .decode()
kg = text2kg(text)
plot_kg(kg)
```

<img width="1612" alt="image" src="https://github.com/arpieb/text2kg/assets/449910/d963c68c-d297-4557-b5e5-1b0694245ddc">

## Maintenance

None.  PoC codebase made available if anyone finds bits of it useful for anything, really.

## License

Yeah, the Unlicense.  I can't really claim much considering I 'Steined&trade; this one together from several different sources and OSS tools.  Use at your own risk; no guarantees, warranties, or any other Ts implied or otherwise.
