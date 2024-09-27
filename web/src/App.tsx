import './App.css';
import { getContainers } from 'services/api';
import ContainerTable from 'components/ContainerTable';
import { useEffect, useState } from 'react';
import { Container } from 'types/Container';

function App() {
  const [containers, setContainers] = useState<Container[]>([]);

  useEffect(() => {
    getContainers().then((containers) => {
      setContainers(containers);
    })
  }, [])

  return (
    <div className="App">
      <ContainerTable rows={containers}/>
    </div>
  );
}

export default App;
