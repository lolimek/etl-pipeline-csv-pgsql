def test_imports():
    import src.ingestion.download_data as dl
    import src.ingestion.load_to_postgres as lp
    assert hasattr(dl, "download_csv")
    assert hasattr(lp, "load_csv_to_table")
