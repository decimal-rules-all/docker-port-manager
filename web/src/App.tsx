import "./App.css";
import { ChangeEventHandler, useEffect, useState } from "react";
import { Container } from "types/Container";
import { getContainers } from "services/api";
import ContainerTable from "components/ContainerTable";
import TitleBar from "components/TitleBar";

function App() {
  const [containers, setContainers] = useState<Container[]>([]);
  const [filteredContainers, setFilteredContainers] = useState<Container[]>([]);

  useEffect(() => {
    getContainers().then((containers) => {
      setContainers(containers);
      setFilteredContainers(containers);
    });
  }, []);

  const searchHandler: ChangeEventHandler<HTMLInputElement> = (e) => {
    const keyword = e.target.value;
    const filteredContainers = containers.filter((container) => {
      return (
        container.id.startsWith(keyword) || container.name.includes(keyword)
      );
    });
    setFilteredContainers(filteredContainers);
  };

  return (
    <div className="App">
      <TitleBar searchHandler={searchHandler} />
      <ContainerTable containers={filteredContainers} />
    </div>
  );
}

export default App;
