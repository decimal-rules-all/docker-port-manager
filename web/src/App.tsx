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
        container.id.includes(keyword) ||
        container.name.includes(keyword) ||
        container.port_bindings.some((pb) => {
          return (
            pb.exposed_port.port.toString().includes(keyword) ||
            pb.exposed_port.protocol.includes(keyword) ||
            pb.host_ports.some((hp) => {
              return (
                hp.host_port.toString().includes(keyword) ||
                hp.host_ip.includes(keyword)
              );
            })
          );
        })
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
