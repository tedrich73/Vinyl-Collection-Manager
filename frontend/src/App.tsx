import { useEffect, useState } from "react";

type RecordItem = {
  id: number;
  title: string;
  artist: number;
  artist_name?: string;
  genres: number[];
  genre_names: string[];
  release_year?: number | null;
  label?: number | null;
  label_name?: string;
  created_at: string
}

function App() {
  const [records, setRecords] = useState<RecordItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/records/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch records")
        }
        return response.json();
      })
      .then((data: RecordItem[]) => {
        setRecords(data);
        setLoading(false)
      })
      .catch((err: Error) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <main>
      <h1>Vinyl Collection</h1>

      {records.length == 0 ? (
        <p>No records yet.</p>
      ) : (
        <ul>
          {records.map((record) => (
            <li key={record.id}>
              <strong>{record.title}</strong>
              {record.artist_name ? ` - ${record.artist_name}`: ""}
              {record.release_year ? ` (${record.release_year})`: ""}
              {record.label_name ? ` - ${record.label_name}`: ""}
              {record.genre_names.length > 0 && ` - ${record.genre_names.join(", ")}`}
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}

export default App;