import Image from 'next/image'
import { mockData } from './mock'
import HallTable from '@/components/HallTable'

export default function Home() {
  return (
    mockData.map(hall => {
      <HallTable hall={hall} />
    })
  )
}