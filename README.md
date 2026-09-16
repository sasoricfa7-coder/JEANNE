# JEANNE

**JEANNE** est un projet d'IA open source visant à fine-tuner un grand modèle de langage (LLM) pour la compréhension et la génération de texte en **Dioula** (langue mandingue parlée au Burkina Faso, en Côte d'Ivoire et au Mali).

Le projet est développé de manière entièrement ouverte, sans financement, et repose sur des ressources cloud gratuites (Google Colab, Kaggle) ainsi que sur des modèles et des données sous licences libres.

---

## 🎯 Objectifs

- Réentraîner un modèle de base performant (DeepSeek) sur un corpus en Dioula.
- Rendre le modèle accessible à la communauté pour des applications éducatives, culturelles ou de recherche.
- Documenter l'ensemble du processus pour permettre à d'autres de reproduire ou d'améliorer le projet.

---

## 📦 Dataset

Le jeu de données utilisé est **Findora/hf_fr_dioula_full**, disponible sur Hugging Face.

- **Lien** : [https://huggingface.co/datasets/Findora/hf_fr_dioula_full/tree/main/data](https://huggingface.co/datasets/Findora/hf_fr_dioula_full/tree/main/data)
- **Contenu** : paires de textes en français et en Dioula, au format `.parquet`.
- **Taille** : environ 10 000 à 100 000 exemples.
- **Licence** : **Apache-2.0**.

Ce dataset est compatible avec la licence AGPLv3+ du projet. Il est utilisé conformément aux conditions de la licence Apache-2.0 (attribution, conservation des mentions de copyright).

---

## 🧠 Modèle de base : DeepSeek

Le modèle de base choisi est la dernière version de **DeepSeek** (ex. DeepSeek-V4-Flash). Il est utilisé via la bibliothèque `transformers` de Hugging Face.

### ⚠️ Licence du modèle DeepSeek

DeepSeek n'est **pas** sous licence AGPL. Il est distribué sous la **DeepSeek License**, une licence open source dérivée de la licence OpenRAIL.

**Ce que cela implique pour JEANNE :**

- **Code du projet** : publié sous **AGPLv3+** (voir section Licence).
- **Poids du modèle DeepSeek** : restent sous la **DeepSeek License**. Vous devez conserver les mentions de copyright et fournir une copie de cette licence à vos utilisateurs.
- **Compatibilité** : la DeepSeek License autorise l'utilisation commerciale, la modification et la redistribution. Elle n'est pas "contagieuse" : vous n'êtes pas obligé de publier votre code sous la même licence. Vous pouvez donc conserver votre code en AGPLv3+ tout en utilisant le modèle DeepSeek.

Pour plus de détails, consultez la [licence officielle DeepSeek](https://github.com/deepseek-ai/DeepSeek-V4-Flash/blob/main/LICENSE).

---

## 📜 Licence du projet

Le code source de JEANNE est distribué sous **GNU Affero General Public License v3.0 ou ultérieure (AGPLv3+)**.

Cela signifie que :
- Vous pouvez utiliser, modifier et distribuer ce logiciel.
- Si vous le rendez accessible via un réseau, vous devez mettre à disposition le code source complet.
- Toute œuvre dérivée doit être placée sous la même licence.

Le texte complet de la licence est disponible dans le fichier `LICENCE/agpl-3.0.md`.

---

## 🛠️ Prérequis

- **Système** : Linux (testé sur Zorin OS / Ubuntu 24.04).
- **Python** : 3.10 ou supérieur.
- **GPU** : NVIDIA avec au moins 16 Go de VRAM (pour l'entraînement QLoRA). Fonctionne aussi sur Google Colab (T4) et Kaggle (T4/P100).

### Installation

```bash
# Créer un environnement virtuel
python3 -m venv ~/venv-llm
source ~/venv-llm/bin/activate

# Installer les dépendances Python
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install transformers datasets peft trl accelerate bitsandbytes huggingface_hub