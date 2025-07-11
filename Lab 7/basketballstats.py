from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(df):
    """Cleans FG, 3PT, and FT columns from makes-attempts format."""
    for col in ['FG', '3PT', 'FT']:
        if col in df.columns:
            # Split into makes and attempts
            makes_attempts = df[col].str.split('-', expand=True).astype(int)
            makes_col = col + 'M'
            attempts_col = col + 'A'
            df[makes_col] = makes_attempts[0]
            df[attempts_col] = makes_attempts[1]
            # Drop the original column
            df.drop(columns=[col], inplace=True)
    return df

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    frame = cleanStats(frame)
    HoopStatsView(frame)

if __name__ == "__main__":
    main()