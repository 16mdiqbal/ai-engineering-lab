from pathlib import Path

import pandas as pd

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data_cache = None  # lazy-loaded cache

    def load_data(self, reload: bool = False, copy: bool = False):
        """
        Load (and cache) the CSV as a DataFrame.

        Parameters
        ----------
        reload : bool, default False
            Force re-reading from disk, refreshing the in-memory cache.
        copy : bool, default False
            Return a defensive copy. Set to True only if the caller intends
            to mutate the returned DataFrame in-place. Keeping this False
            avoids unnecessary memory usage on large datasets.

        Notes
        -----
        Returning the cached DataFrame directly is safe if callers treat it
        as read-only. Mutators should either:
          * request a copy via `copy=True`, or
          * explicitly call `invalidate_cache()` then `load_data(reload=True)`
            after external modifications to the source file.
        """
        if reload or self._data_cache is None:
            try:
                self._data_cache = pd.read_csv(self.file_path)
                print(f"Data loaded from disk: {Path(self.file_path).resolve()}")
            except FileNotFoundError as e:
                # Raise a clear error instead of returning None to avoid hidden NoneType issues downstream
                raise FileNotFoundError(f"CSV file not found: {self.file_path}") from e
        else:
            # Using cached version
            print("Using cached data.")
        return self._data_cache.copy() if (copy and self._data_cache is not None) else self._data_cache

    def invalidate_cache(self):
        """Invalidate the current cached DataFrame forcing next load to hit disk."""
        self._data_cache = None


    def export_data(self, df: pd.DataFrame, output_path: str):
        """ Export DataFrame to CSV file """
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out, index=False)
        print(f"Data exported to {out.resolve()}")