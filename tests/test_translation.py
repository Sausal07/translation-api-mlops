from fastapi.testclient import TestClient

from app.main import app


def fake_init_model():
    pass


def fake_pass_variable(ip):
    pass


def fake_translation_model(
    ip_text,
    srcLang,
    tgtLang,
    delimiter,
    nSuggestions
):
    return ["नमस्ते"]

def fake_ilil_translation_model(
    ip_text,
    srcLang,
    tgtLang,
    delimiter,
    nSuggestions
):
    return ["नमस्ते"]

def fake_unsupported_translation(
    ip_text,
    srcLang,
    tgtLang,
    delimiter,
    nSuggestions
):
    return "Currently this web service is not supporting"


app.dependency_overrides = {}


def test_translation_eng_to_hin(monkeypatch):

    monkeypatch.setattr(
        "app.main.initModeltranslation",
        fake_init_model
    )

    monkeypatch.setattr(
        "app.main.pass_variable",
        fake_pass_variable
    )

    monkeypatch.setattr(
        "app.main.translation_model_multi",
        fake_translation_model
    )

    client = TestClient(app)

    payload = {
        "ip_text": "Hello",
        "srcLang": "eng-latn",
        "tgtLang": "hin-dev",
        "delimiter": " ",
        "nSuggestions": 1
    }

    response = client.post(
        "/getTranslation",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "Output" in data
    assert data["Output"] == ["नमस्ते"]



def test_translation_il_il(monkeypatch):

    monkeypatch.setattr(
        "app.main.initModeltranslation",
        fake_init_model
    )

    monkeypatch.setattr(
        "app.main.pass_variable",
        fake_pass_variable
    )

    monkeypatch.setattr(
        "app.main.translation_model_ILIL",
        fake_ilil_translation_model
    )

    client = TestClient(app)

    payload = {
        "ip_text": "नमस्ते",
        "srcLang": "hin-dev",
        "tgtLang": "mar-dev",
        "delimiter": " ",
        "nSuggestions": 1
    }

    response = client.post(
        "/getTranslation",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "Output" in data
    assert data["Output"] == ["नमस्ते"]


def test_translation_missing_ip_text():

    payload = {
        "srcLang": "eng-latn",
        "tgtLang": "hin-dev",
        "delimiter": " ",
        "nSuggestions": 1
    }

    client = TestClient(app)

    response = client.post(
        "/getTranslation",
        json=payload
    )

    assert response.status_code == 422


def test_unsupported_language_pair(monkeypatch):

    monkeypatch.setattr(
        "app.main.initModeltranslation",
        fake_init_model
    )

    monkeypatch.setattr(
        "app.main.pass_variable",
        fake_pass_variable
    )

    monkeypatch.setattr(
        "app.main.translation_model_multi",
        fake_unsupported_translation
    )

    client = TestClient(app)

    payload = {
        "ip_text": "Hello",
        "srcLang": "eng-latn",
        "tgtLang": "xyz",
        "delimiter": " ",
        "nSuggestions": 1
    }

    response = client.post(
        "/getTranslation",
        json=payload
    )

    assert response.status_code == 401

    data = response.json()

    assert data["error"] == "Invalid Input language pairs"