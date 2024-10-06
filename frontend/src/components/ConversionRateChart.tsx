// MyLineChart.tsx
import { Chart, ChartData, registerables } from 'chart.js';
import React, { useEffect, useMemo, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { BACKEND_URL } from '../constants/constants';

Chart.register(...registerables);

interface Data {
  timestamp: Date;
  timestampString: string;
  value: number;
}

const ConversionRateChart: React.FC = () => {
  const [data, setData] = useState<Data[]>([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch(BACKEND_URL)
        .then((response) =>
          response.json().then((jsonBody) => {
            const conversionRate = jsonBody.data;
            const curDate = new Date();
            setData((prev) => {
              if (prev.length > 0) {
                // don't set if somehow older date response just returned
                const lastTimestamp = prev[prev.length - 1].timestamp;
                if (lastTimestamp > curDate) {
                  return prev;
                }
              }
              return [
                ...prev,
                {
                  timestampString: curDate.toLocaleTimeString(),
                  value: conversionRate,
                  timestamp: curDate,
                },
              ].slice(-10);
              // taking last 10 datapoints
            });
          })
        )
        .catch((error) => {
          console.error(error);
        });
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const chartData: ChartData<'line'> = useMemo(() => {
    return {
      labels: data.map((dataPoint) => dataPoint.timestampString),
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
          },
        },
        scales: {
          y: {
            min: 0.9,
            max: 1.2,
          },
        },
      }}
    />
  );
};

export default ConversionRateChart;
