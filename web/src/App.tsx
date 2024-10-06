import './App.css';
import { useEffect, useState } from 'react';
import { Container } from 'types/Container';
import { getContainers } from 'services/api';
import ContainerTable from 'components/ContainerTable';
import TitleBar from 'components/TitleBar';

function App() {
  const [containers, setContainers] = useState<Container[]>([]);

  useEffect(() => {
    getContainers().then((containers) => {
      setContainers(containers);
    })
  }, [])

  return (
    <div className="App">
      <TitleBar />
      <ContainerTable rows={containers}/>
    </div>
  );
}

export default App;
