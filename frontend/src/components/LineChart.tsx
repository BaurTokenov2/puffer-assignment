// MyLineChart.tsx
import { Chart, ChartData, registerables } from 'chart.js';
import React, { useEffect, useMemo, useState } from 'react';
import { Line } from 'react-chartjs-2';

Chart.register(...registerables);

interface Data {
  timestamp: string;
  value: number;
}

const MyLineChart: React.FC = () => {
  const [data, setData] = useState<Data[]>([]);

  useEffect(() => {
    const interval = setInterval(() => {
      const curDate = new Date();

      setData((prev) =>
        [
          ...prev,
          {
            timestamp: curDate.toLocaleTimeString(),
            value: Math.floor(Math.random() * 100),
          },
        ].slice(-10)
      );
    }, 5000);

    return () => clearInterval(interval);
  }, []);
  console.log(data);

  const chartData: ChartData<'line'> = useMemo(() => {
    return {
      labels: data.map((dataPoint) => dataPoint.timestamp),
      datasets: [
        {
          label: 'Conversion Rate',
          data: data.map((dataPoint) => dataPoint.value),
          backgroundColor: ['#7900db'],
          borderColor: '#7900db',
          borderWidth: 2,
        },
      ],
    };
  }, [data]);

  return (
    <Line
      data={chartData}
      options={{
        plugins: {
          title: {
            display: true,
            text: 'Puffer Conversion Rate',
            fullSize: true,
          },
        },
        scales: {
          y: {
            min: 0,
            max: 100,
          },
        },
      }}
    />
  );
};

export default MyLineChart;
