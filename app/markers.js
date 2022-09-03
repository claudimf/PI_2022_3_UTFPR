const fontAwesomeIcon = L.divIcon({
    html: '<i class="fa fa-map fa-4x"></i>',
    iconSize: [60, 60],
    className: 'myDivIcon'
});

var marker = L.marker([-1.397746, -48.473087],)
.bindPopup('<div><h3><i class="fa fa-building fa-3x" aria-hidden="true"></i>&emsp;&emsp;&emsp;Empresa - AFFA ENGENHARIA E ARQUITETURA LTDA</h3><p><b>Município - </b>Belém<br><b>UF - </b>PA<br><b>Endereço - </b>Av. Brasil, 208 - Val-de-Cans, Belém - PA, 66617-300</p></div><div><h3><i id="icon2"class="fa fa-address-book fa-3x" aria-hidden="true"></i>&nbsp;&nbsp;Contratações</div><br><div id="scrollbar"><b>Arquivista: </b>3<br><b>Auxiliar Administrativo: </b>3<br><b>Auxiliar Apoio Operaciona: </b>1<br><b>Desenhista Mecanico: </b>1<br><b>Desenhista Projetista: </b>1<br><b>Engenheiro de Automação: </b>1<br><b>Engenheiro Mecânico: </b>3<br><b>Engenheiro: </b>1<br><b>Engenheiro Eletricista: </b>2<br><b>Insp. De Fisc Eletrica Sen: </b>1<br><b>Insp. Fiscal Civil Pleno: </b>1<br><b>Insp. De Eletrica: </b>1<br><b>Insp. De Planejamento: </b>1<br><b>Inspetor: </b>1<br><b>Inspetor  Senior: </b>1<br><b>Inspetor Obras Servicos P: </b>1<br><b>Motorista: </b>3<br><b>Planejador: </b>1<br><b>Projetista: </b>9<br><b>Tec.Segurança Trabalho Es: </b>2<br><b>Tecnico Medicao: </b>1</div><br><b>Total de contratações: </b>39<br><div><h3><i id="icon3" class="fa fa-map-marker fa-3x" aria-hidden="true"></i>&nbsp;&nbsp;Município das pessoas contratadas</h3><br>Não informado')
.addTo(map);

var marker = L.marker([-1.526732, -48.703178])
.bindPopup('<div><h3><i class="fa fa-building fa-3x" aria-hidden="true"></i>&emsp;&emsp;&emsp;Empresa - ALLES SERVIÇOS</h3><b><p></b><b>Município - </b>Barcarena<br><b>UF - </b>PA<br><b>Endereço - </b>Av. Padre Casemiro Pereira Souza, PE 198 - Núcleo Urbano, Barcarena - PA,  68445-000</p></div><div><h3><i id="icon2"class="fa fa-address-book fa-3x" aria-hidden="true"></i>&nbsp;&nbsp;Contratações</div><br><div id="scrollbar"><br>Não informado</div><br><b>Total de contratações: </b>66<br><h3><i id="icon3" class="fa fa-map-marker fa-3x" aria-hidden="true"></i>&nbsp;&nbsp;Município das pessoas contratadas</h3><br>Não informado')
.addTo(map);
