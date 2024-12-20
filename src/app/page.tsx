import { MainForm } from "@/components/form/main-form";
import { ToggleTheme } from "@/components/theme/toggle-theme";
import { getURL } from "@/utils/getURL";
import axios from "axios";
import { Suspense } from "react";

export default async function Home() {
  const URL = getURL();

  
  const data = await axios.get(`${URL}/py/helloWorld`);



  return (
    <div className="flex w-full h-screen items-center justify-center">
          <MainForm/>
          <Suspense>
            <ToggleTheme/>
          </Suspense>
    </div>
  );
}
